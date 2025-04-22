# Montage Vidéo Automatisé avec IA

Ce projet permet de créer automatiquement une version raccourcie d'une vidéo en sélectionnant les meilleurs moments grâce à l'IA.

## Prérequis

- Python 3.8 ou supérieur
- Une clé API OpenAI

## Installation

1. Clonez ce dépôt
2. Installez les dépendances :
```bash
pip install -r requirements.txt
```
3. Créez un fichier `.env` et ajoutez votre clé API OpenAI :
```
OPENAI_API_KEY=votre_clé_api_ici
```

## Utilisation

1. Placez votre vidéo dans le dossier du projet et renommez-la en `input_video.mp4` (ou modifiez le chemin dans le code)
2. Exécutez le script :
```bash
python video_editor.py
```

Le script va :
1. Transcrire la vidéo avec Whisper
2. Envoyer le transcript à GPT-4 pour sélectionner les meilleurs moments
3. Créer une nouvelle vidéo avec uniquement ces moments

La vidéo finale sera sauvegardée sous le nom `highlight_video.mp4`

## Notes

- Le modèle Whisper utilisé est "base" pour des performances rapides. Vous pouvez le changer pour "small" ou "medium" pour une meilleure précision
- Le processus peut prendre du temps selon la longueur de la vidéo
- Assurez-vous d'avoir suffisamment d'espace disque pour les fichiers temporaires 