from django.forms import ModelForm
from django import forms
from .models import UserChat
from django.contrib.auth.models import User


class ChatAddForm(ModelForm):
    users = ((user.pk, user.username) for user in User.objects.order_by('username'))
    interlocutor = forms.CharField(widget=forms.Select(choices=users))

    def __init__(self, user, *args):
        ModelForm.__init__(self)
        self.user = user

    class Meta:
        model = UserChat
        fields = ('user', 'interlocutor')
