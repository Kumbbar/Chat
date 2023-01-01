from django.db import models
from django.contrib.auth.models import User


class MessageStatus(models.Model):
    name = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'messages_status'


class Message(models.Model):
    text = models.TextField(max_length=400, null=False)
    user_sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_sender')
    user_receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user_receiver')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'messages'
 