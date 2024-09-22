from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import speech_recognition as sr
import wave

@csrf_exempt
def transcribe_audio(request):
    if request.method == 'POST':
        # Assuming audio data is sent as a file
        audio_file = request.FILES['audio']
        with wave.open(audio_file, 'rb') as wf:
            recognizer = sr.Recognizer()
            audio_data = sr.AudioFile(audio_file)
            with audio_data as source:
                audio = recognizer.record(source)
            try:
                # Use CMU Sphinx for offline recognition
                text = recognizer.recognize_sphinx(audio)
                return JsonResponse({'transcription': text})
            except sr.UnknownValueError:
                return JsonResponse({'error': 'Could not understand audio'}, status=400)
            except sr.RequestError as e:
                return JsonResponse({'error': f'Could not request results; {e}'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)