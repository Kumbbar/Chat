import json

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'messages/index.html', {})


@login_required
def room(request, room_name):
    print(mark_safe(json.dumps(room_name)))
    return render(request, 'messages/room.html', {})
