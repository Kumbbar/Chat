from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from channels.http import AsgiRequest
from .services.chats import UsersChatsService
from .services.decorators import except_bad_requests


@login_required
def chats(request: AsgiRequest) -> render:
    user_chats = UsersChatsService.get_user_chats(request)
    return render(request, 'messages/chats.html', {'user_chats': user_chats})


@login_required
def add_chat_page(request: AsgiRequest) -> redirect:
    return render(request, 'messages/add_chat.html')


@login_required
@except_bad_requests
def add_chat(request: AsgiRequest, username: str) -> redirect:
    UsersChatsService.create_chat(request, username)
    return redirect('messages:chats')


@login_required
def add_chat_search(request: AsgiRequest) -> render:
    username_find = request.GET.get('username') if request.GET.get('username') else ''

    users = UsersChatsService.get_users_without_chat(request, username_find)
    return render(request, 'messages/chat_list.html', {'users': users})


@login_required
def dialog(request: AsgiRequest, room_name: str):
    return render(request, 'messages/room.html', {})
