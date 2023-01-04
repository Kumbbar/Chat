from django.forms import ModelForm
from django import forms
from .models import UserChat
from django.contrib.auth.models import User


class ChatAddForm(ModelForm):
    users = ((user, user.username) for user in User.objects.order_by('username'))
    user2 = forms.CharField(widget=forms.Select(choices=users))

    def __init__(self, current_username: str = None, *args, **kw):
        """Must set current_username for POST method"""
        super().__init__(*args, **kw)
        if current_username:
            self.user1 = User.objects.get(username=current_username)

    class Meta:
        model = UserChat
        fields = ('user1', 'user2')
