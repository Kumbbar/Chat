from django.db import models
from django.contrib.auth.models import User


class UserChat(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1', null=False)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2', null=False)

    class Meta:
        db_table = 'user_chats'
        unique_together = ('user1', 'user2')


class MessageStatus(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'message_statuses'


class Message(models.Model):
    text = models.TextField(max_length=400, null=False)
    user_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sender', null=False)
    user_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_receiver', null=False)
    message_status = models.ForeignKey(MessageStatus, on_delete=models.SET_NULL, null=True)
    chat = models.ForeignKey(UserChat, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'

    def __str__(self):
        return f'{self.text}'
