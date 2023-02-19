from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from channels.http import AsgiRequest

from .services.db_logic import UserChatsService, MessageService
from .services.decorators import except_bad_requests
from .filters import *

# Chats views


@login_required
def chats(request: AsgiRequest) -> render:
    user_chats = UserChatsService.get_user_chats(request.user)
    return render(
        request, 'messages/chats.html',
        {'user_chats': user_chats}
    )


@login_required
def add_chat_page(request: AsgiRequest) -> redirect:
    return render(request, 'messages/add_chat.html')


@login_required
@except_bad_requests
def add_chat(request: AsgiRequest, username: str) -> redirect:
    UserChatsService.create_chat(request.user, username)
    return redirect('messages:chats')


@login_required
def add_chat_search(request: AsgiRequest) -> render:
    username_find = request.GET.get('username') if request.GET.get('username') else ''

    users = UserChatsService.get_users_without_chat(request.user, username_find)
    return render(request, 'messages/chat_list.html', {'users': users})


# Room views

@login_required
def chat_room(request: AsgiRequest, interlocutor: str):
    messages = MessageService.get_and_read_chat_messages(request.user, interlocutor)
    return render(
            request, 'messages/chat_room.html',
            {'interlocutor': interlocutor, 'messages': messages}
        )
