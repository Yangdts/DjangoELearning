from django.urls import re_path
from . import consumers

# use regex to match path
websocket_urlpatterns = [
    re_path(r'ws/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]