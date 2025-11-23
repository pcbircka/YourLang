import openai

def transcribe_audio(audio_path: str) -> str:
    with open(audio_path, "rb") as audio:
        response = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )
    return response.text
