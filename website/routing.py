from django.urls import re_path
from . import consumers

# re_path is a more advanced version of path that allows you to pass more complex URL patterns to your application.
# With the ASGI version of Django, you need to use re_path instead of path, because this a diffrent technology.
# Which use routing instead of urls.py and consumers instead of views.py

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$",
            consumers.ChatRoomConsumer.as_asgi()),
]
