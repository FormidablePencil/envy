from django.urls import path, include
from hello_world.core.views import home

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('ws/', include('your_websocket_app.urls')),  # Add WebSocket URL routing
]
