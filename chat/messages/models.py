from django.db import models
from django.contrib.auth.models import User


class MessageStatus(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'message_statuses'


class Message(models.Model):
    text = models.TextField(max_length=400, null=False)
    user_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sender')
    user_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_receiver')
    message_status_id = models.ForeignKey(MessageStatus, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'


class UserDialog(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')

    class Meta:
        db_table = 'user_dialogs'

