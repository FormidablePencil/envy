from django.http import JsonResponse
from django.shortcuts import render

# Example view to demonstrate access levels

def example_view(request):
    return JsonResponse({'message': 'This is an example view for access levels.'})

# Home view

def home(request):
    return render(request, 'index.html')  # Render the index.html template
