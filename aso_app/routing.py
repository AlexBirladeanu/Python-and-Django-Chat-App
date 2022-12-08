from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('', consumers.ChatConsumer.as_asgi())
]
