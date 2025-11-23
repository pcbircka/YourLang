from whisper_service import transcribe_audio
import sys

def main():
    audio_path = sys.argv[1]
    text = transcribe_audio(audio_path)
    print("Распознанный текст:")
    print(text)

if __name__ == "__main__":
    main()

