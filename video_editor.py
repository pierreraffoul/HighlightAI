import whisper
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from dotenv import load_dotenv
from openai import OpenAI

def load_environment():
    """Charge les variables d'environnement depuis le fichier .env"""
    load_dotenv()

def transcribe_video(video_path):
    """Transcrit la vidéo et retourne les segments avec timestamps"""
    print("Chargement du modèle Whisper...")
    model = whisper.load_model("base")
    print("Transcription en cours...")
    result = model.transcribe(video_path, verbose=True)
    return result["segments"]

def format_transcript_for_gpt(segments):
    """Formate le transcript pour l'API GPT"""
    transcript = ""
    for segment in segments:
        transcript += f"[{segment['start']} - {segment['end']}] {segment['text']}\n"
    return transcript

def get_best_moments(transcript):
    """Envoie le transcript à GPT pour sélectionner les meilleurs moments"""
    prompt = f"""
    Voici le transcript d'une vidéo avec ses timestamps.

Voici la transcription d'une vidéo de quelqu'un qui parle pendans 1h.
La vidéo dure 1h car la vidéo n'est pas coupée. Cependant son contenu ne devrait pas etre aussi long.
Ton but est de couper les moments les moins intéressants afin d'avoir une vidéo fluide à regarder.
La vidéo finale doit faire une dizaine de minutes.


    Transcript :
    {transcript}

    Réponds uniquement avec une liste comme :
    [[5.0, 10.0], [45.0, 50.0], ...]
    """

    client = OpenAI()  # Se base sur la variable OPENAI_API_KEY de l'environnement
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return eval(response.choices[0].message.content)

def create_highlight_video(video_path, timestamps, output_path):
    """Crée une vidéo avec uniquement les moments sélectionnés"""
    print("Création de la vidéo finale...")
    video = VideoFileClip(video_path)
    clips = [video.subclip(start, end) for start, end in timestamps]
    final = concatenate_videoclips(clips)
    final.write_videofile(output_path)
    print(f"Vidéo finale sauvegardée dans : {output_path}")

def main():
    load_environment()

    video_path = "LARGENT.mp4"
    output_path = "highlight_video.mp4"

    segments = transcribe_video(video_path)
    transcript = format_transcript_for_gpt(segments)
    best_moments = get_best_moments(transcript)
    create_highlight_video(video_path, best_moments, output_path)

if __name__ == "__main__":
    main()
