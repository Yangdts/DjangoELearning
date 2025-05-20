import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # receive message from user
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # echo message back to user for adding to chat log
        self.send(text_data=json.dumps({
            'message': message
        }))
