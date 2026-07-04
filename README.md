# Ollama AI Part

A Flask-based backend application that integrates GPT-OSS via Ollama Cloud to perform AI-powered text processing tasks.

## Features

- Echo API
- Text Summarization
- Rewrite text in different tones
- Generate learning check questions
- Analyze user activity

## Tech Stack

- Python
- Flask
- Ollama Cloud
- GPT-OSS
- Thunder Client

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure your environment variables (if required)
5. Run:
   ```bash
   python app.py
   ```

## API Endpoints

- `GET /health`
- `POST /echo`
- `POST /summary`
- `POST /rewrite-tone`
- `POST /learning-check`
- `POST /key-points`
- `POST /analyze-user-activity`
