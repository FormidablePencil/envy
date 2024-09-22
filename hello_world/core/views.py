from django.shortcuts import render
import subprocess

def index(request):
    context = {
        "title": "Django example",
    }
    return render(request, "index.html", context)

def run_flet_app(request):
    subprocess.Popen(["python3", "hello_world/core/flet_app.py"])
    return render(request, "index.html", {"title": "Flet app running"})
