from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .services.db_logic import MessageService


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        MessageService.create_message_by_usernames(message, sender, receiver)


        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
                'receiver': receiver
            }
        )

    def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        receiver = event['receiver']

        self.send(text_data=json.dumps({
            'event': "Send",
            'message': message,
            'sender': sender,
            'receiver': receiver
        }))
