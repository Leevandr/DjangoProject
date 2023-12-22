from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from mychat.chat.consumers import ChatConsumer

application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/chat/", ChatConsumer.as_asgi()),
                ]
            )
        ),
    }
)
