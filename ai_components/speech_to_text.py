import pocketsphinx

class SpeechToText:
    def __init__(self):
        self.recognizer = pocketsphinx.Pocketsphinx()

    def transcribe_audio(self, audio_file):
        try:
            text = self.recognizer.decode_raw(audio_file)
            return text
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return None