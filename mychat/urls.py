from django.contrib import admin
from django.urls import path, include
from mychat.chat.routing import websocket_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... другие URL-шаблоны вашего приложения ...
    path('ws/chat/', include(websocket_urlpatterns)),
    # ... другие URL-шаблоны вашего приложения ...
]
