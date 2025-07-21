from flask import Flask, request, send_file, jsonify
from TTS.api import TTS
import os

app = Flask(__name__)

tts = TTS("tts_models/id/glow-tts")

@app.route("/")
def home():
    return jsonify({"message": "Coqui TTS API is running"})

@app.route("/tts", methods=["POST"])
def tts_api():
    text = request.form.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    output_path = "output.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return send_file(output_path, mimetype="audio/wav")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
