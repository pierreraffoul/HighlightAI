import whisper
import openai
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from dotenv import load_dotenv

def load_environment():
    """Charge les variables d'environnement depuis le fichier .env"""
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

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
    Voici le transcript d'une vidéo avec les timestamps. Ta tâche est d'en sélectionner uniquement les meilleurs moments (les plus intéressants, drôles, percutants, ou émotionnels). Renvoie uniquement une liste de timestamps [start, end] des moments choisis.

    Transcript :
    {transcript}

    Réponds uniquement avec une liste comme :
    [[5.0, 10.0], [45.0, 50.0], ...]
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return eval(response['choices'][0]['message']['content'])

def create_highlight_video(video_path, timestamps, output_path):
    """Crée une vidéo avec uniquement les moments sélectionnés"""
    print("Création de la vidéo finale...")
    video = VideoFileClip(video_path)
    clips = [video.subclip(start, end) for start, end in timestamps]
    final = concatenate_videoclips(clips)
    final.write_videofile(output_path)
    print(f"Vidéo finale sauvegardée dans : {output_path}")

def main():
    # Configuration
    load_environment()
    
    # Chemins des fichiers
    video_path = "input_video.mp4"  # À modifier selon votre vidéo
    output_path = "highlight_video.mp4"
    
    # Processus
    segments = transcribe_video(video_path)
    transcript = format_transcript_for_gpt(segments)
    best_moments = get_best_moments(transcript)
    create_highlight_video(video_path, best_moments, output_path)

if __name__ == "__main__":
    main() 