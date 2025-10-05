# Python Voice Assistant

This project is a simple AI-powered voice assistant built with Python. It listens to your voice, understands your request using AI, and responds both with spoken voice and text output.

## Features
- Speech recognition (voice to text)
- AI-powered response (OpenAI API)
- Text-to-speech (voice output)
- Command/text output

## Requirements
- Python 3.8+
- Internet connection (for OpenAI API)

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Run the assistant:
   ```bash
   python main.py
   ```

## Usage
Speak your request when prompted. The assistant will reply with both text and voice.

---
This is a basic starting point. You can extend it with more commands and integrations as needed.
