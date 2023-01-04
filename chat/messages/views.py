import json
from .forms import ChatAddForm
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from .forms import ChatAddForm
from django.contrib.auth.models import User


@login_required
def index(request) -> render:
    return render(request, 'messages/chats.html', {'form': ChatAddForm()})


@login_required
def add_chat(request) -> redirect:
    if request.method == 'POST':
        form = ChatAddForm(data=request.POST, current_username=request.user.username)
        if form.is_valid():
            pass
            # print(form.user2)
    return redirect('messages:index')


@login_required
def dialog(request, room_name):
    return render(request, 'messages/room.html', {})
