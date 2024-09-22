from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hello_world.core import views as core_views

urlpatterns = [
    path("", core_views.index),
    path("flet/", core_views.run_flet_app, name="run_flet"),
    path("admin/", admin.site.urls),
    path("__reload", include("django_browser_reload.urls")),
    path("ai_manager/", include("hello_world.ai_manager.urls")),  # Include AI Manager URLs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
