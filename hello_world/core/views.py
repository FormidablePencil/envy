from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess
import wave
import speech_recognition as sr

# Function to render the index page

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

# Function to run the Flet app

def run_flet_app(request):
    # Start the Flet app in a separate process
    subprocess.Popen(["python3", "hello_world/core/flet_app.py"])
    return render(request, "index.html", {"title": "Flet app running"})

# Function to handle audio transcription requests
@csrf_exempt
def transcribe_audio(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio']
        with wave.open(audio_file, 'rb') as wf:
            recognizer = sr.Recognizer()
            audio_data = sr.AudioFile(audio_file)
            with audio_data as source:
                audio = recognizer.record(source)
            try:
                text = recognizer.recognize_sphinx(audio)
                return JsonResponse({'transcription': text})
            except sr.UnknownValueError:
                return JsonResponse({'error': 'Could not understand audio'}, status=400)
            except sr.RequestError as e:
                return JsonResponse({'error': f'Could not request results; {e}'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
