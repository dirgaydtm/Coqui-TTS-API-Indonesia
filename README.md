# Coqui TTS API (Bahasa Indonesia)

API sederhana untuk Text-to-Speech (TTS) Bahasa Indonesia menggunakan Coqui TTS dan Flask.

## Fitur

- Endpoint `/` untuk cek status API
- Endpoint `/tts` untuk mengubah teks menjadi audio (WAV)

## Instalasi

1. **Clone repository**
   ```bash
   git clone <repo-url>
   cd coqui
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

## Cara Menjalankan

```bash
python app.py
```

API akan berjalan di `http://localhost:5000` (atau port lain sesuai environment variable `PORT`).

## Penggunaan API

### 1. Cek Status

- **Endpoint:** `GET /`
- **Response:**
  ```json
  { "message": "Coqui TTS API is running" }
  ```

### 2. Text-to-Speech

- **Endpoint:** `POST /tts`
- **Form Data:**
  - `text`: Teks yang ingin diubah menjadi suara
- **Response:**
  - File audio WAV hasil konversi

#### Contoh dengan `curl`:

```bash
curl -X POST -F "text=Halo, apa kabar?" http://localhost:5000/tts --output output.wav
```

## Deployment

Untuk deployment (misal di Heroku), pastikan file `Procfile` sudah ada:

```
web: python app.py
```
