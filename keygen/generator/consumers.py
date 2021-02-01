import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class KeyConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        if not self.user.is_authenticated:
            self.close(code=403)
        async_to_sync(self.channel_layer.group_add)(
            'online_users',
            self.channel_name
        )
        self.accept()
    
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'online_users',
            self.channel_name
        ) 

    def new_key(self, event):
        key = event['key']
        last_updated = event['last_updated']
        self.send(text_data=json.dumps({
            'key': key,
            'last_updated': last_updated,
        }))