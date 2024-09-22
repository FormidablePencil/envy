import flet as ft
from flet import Page, ElevatedButton, Text, Column
import requests
import wave
import os
from vosk import Model, KaldiRecognizer
import threading

# Function to send audio file to Django API

def send_audio_to_api(audio_file):
    url = 'http://127.0.0.1:8000/ai_manager/transcribe/'  # Update with your API endpoint
    with open(audio_file, 'rb') as file:
        response = requests.post(url, files={'audio': file})
        return response.json()

# Function to recognize speech from audio using Vosk
def recognize_speech_from_audio(audio_file, transcription_text):
    if not os.path.exists(audio_file):
        transcription_text.value = "Error: Audio file does not exist."
        transcription_text.update()
        print(f"Error: Audio file does not exist at {audio_file}")  # Log error
        return
    print(f"Using audio file: {audio_file}")  # Log the audio file path
    model = Model("vosk-model/vosk-model-small-en-us-0.15")  # Update with the path to your Vosk model
    recognizer = KaldiRecognizer(model, 16000)
    with wave.open(audio_file, "rb") as wf:
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                transcription_text.value += result
                transcription_text.update()
                print(f"Transcription result: {result}")  # Log transcription result
    final_result = recognizer.FinalResult()
    transcription_text.value += final_result
    transcription_text.update()
    print(f"Final transcription result: {final_result}")  # Log final result

# Main entry point for the Flet app
async def main(page: Page):
    page.title = "Audio Recorder"
    page.window.width = 600
    page.window.height = 400
    page.window.resizable = False

    audio_rec = ft.AudioRecorder(
        audio_encoder=ft.AudioEncoder.WAV,
        on_state_changed=lambda state: print(f"Audio Recorder State: {state}")
    )
    page.overlay.append(audio_rec)

    transcription_text = Text('Transcription will appear here.')
    page.add(transcription_text)

    def start_transcription():
        recognize_speech_from_audio('recorded_audio.wav', transcription_text)

    start_button = ElevatedButton(
        text="Start Audio Recorder",
        on_click=lambda e: audio_rec.start_recording(output_path='recorded_audio.wav') or threading.Thread(target=start_transcription).start(),
    )
    stop_button = ElevatedButton(
        text="Stop Audio Recorder",
        on_click=lambda e: audio_rec.stop_recording(),
    )
    upload_button = ElevatedButton(
        text="Upload Audio",
        on_click=lambda e: send_audio_to_api('recorded_audio.wav'),
    )

    page.add(start_button, stop_button, upload_button, transcription_text)  # Add buttons to the page

if __name__ == "__main__":
    ft.app(target=main, port=9000)