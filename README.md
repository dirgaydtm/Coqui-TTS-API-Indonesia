# Coqui TTS API (Indonesian Language)

Simple API for Indonesian Text-to-Speech (TTS) using Coqui TTS (`tts_models/id/glow-tts`) and Flask.

## Features

- `/` endpoint for API status check
- `/tts` endpoint to convert text to audio (WAV)
- Uses Indonesian TTS model from Coqui TTS

## Installation

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd coqui
   ```
2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Make sure ffmpeg and git are installed**
   - For Docker users, these dependencies are installed automatically.

## How to Run

### Development Mode

```bash
python app.py
```

The API will run at `http://localhost:5000` (or another port according to the `PORT` environment variable).

### Production Mode (recommended)

Run with Gunicorn:

```bash
gunicorn app:app --bind 0.0.0.0:5000
```

Or use Docker:

```bash
docker build -t coqui-tts-api .
docker run -p 5000:5000 coqui-tts-api
```

## API Usage

### 1. Status Check

- **Endpoint:** `GET /`
- **Response:**
  ```json
  { "message": "Coqui TTS API is running" }
  ```

### 2. Text-to-Speech

- **Endpoint:** `POST /tts`
- **Form Data:**
  - `text`: Text to be converted to speech
- **Response:**
  - WAV audio file of the conversion result

#### Example using `curl`:

```bash
curl -X POST -F "text=Hello, how are you?" http://localhost:5000/tts --output output.wav
```

## Deployment

For deployment (e.g., on Heroku), make sure the `Procfile` exists:

```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

---

**Notes:**

- The API port can be changed using the `PORT` environment variable.
- Make sure your server has enough resources to run the TTS model.
