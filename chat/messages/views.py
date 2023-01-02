import json
from .forms import ChatAddForm
from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .forms import ChatAddForm

@login_required
def index(request) -> render:
    return render(request, 'messages/chats.html', {'form': ChatAddForm()})

@login_required
def add_chat(request) -> render:
    if request.method == 'POST':
        form = ChatAddForm(user=request.user, data=request.POST)
        if form.is_valid():
            print(form.interlocutor)


@login_required
def dialog(request, room_name):
    return render(request, 'messages/room.html', {})
