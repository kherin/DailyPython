# routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels_app.consumers import Consumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws/chat/", Consumer.as_asgi()),
    ]),
})
