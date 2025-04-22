# AI Video Highlight Generator

This project automatically creates a shortened version of a video by selecting the best moments using AI.

## Prerequisites

- Python 3.8 or higher
- An OpenAI API key
- FFmpeg (required for video processing)

### Installing FFmpeg

#### Windows:
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract the downloaded zip file
3. Add the `bin` folder to your system PATH:
   - Open System Properties > Advanced > Environment Variables
   - Under "System Variables", find and select "Path"
   - Click "Edit" and add the path to the FFmpeg bin folder
   - Click "OK" to save changes

#### Linux:
```bash
sudo apt update
sudo apt install ffmpeg
```

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your video in the project directory and rename it to `test.mp4` (or modify the path in the code)
2. Run the script:

#### Windows:
```bash
python video_editor.py
```

#### Linux:
```bash
python3 video_editor.py
```

The script will:
1. Transcribe the video using Whisper
2. Send the transcript to GPT-4 to select the best moments
3. Create a new video containing only these moments

The final video will be saved as `highlight_video.mp4`

## Notes

- The Whisper model used is "base" for faster performance. You can change it to "small" or "medium" for better accuracy
- The process may take some time depending on the video length
- Make sure you have enough disk space for temporary files
- For Windows users: If you encounter any FFmpeg-related errors, ensure FFmpeg is properly installed and added to your PATH 