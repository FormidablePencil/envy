from django.urls import path
from hello_world.core.views import home

urlpatterns = [
    path('', home, name='home'),  # Home view
]
