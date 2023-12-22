# mychat/mychat/urls.py
from django.contrib import admin
from django.urls import path, include

from mychat.chat.routing import websocket_urlpatterns  # Импортируйте URL-шаблоны WebSocket

urlpatterns = [
    path('admin/', admin.site.urls),
    # ...
    path('ws/chat/', include(websocket_urlpatterns)),
    # ...
]
