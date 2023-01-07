from channels.http import AsgiRequest
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.http import HttpResponseBadRequest
from .exceptions import ChatExistsException
from ..models import UserChat
from django.db.models import Q


class UsersChatsService:
    @classmethod
    def is_chat_exists(cls, current_user: User, interlocutor: User) -> bool:
        return True if UserChat.objects.filter(
                Q(user1=current_user, user2=interlocutor) |
                Q(user2=current_user, user1=interlocutor)
            ).first() or current_user == interlocutor else False

    @classmethod
    def get_user_chats(cls, request: AsgiRequest) -> QuerySet:
        user = request.user
        chats = UserChat.objects.filter(Q(user1=user) | Q(user2=user))
        return chats

    @classmethod
    def get_users_without_chat(cls, request: AsgiRequest, username_find: str) -> QuerySet:
        current_user = request.user
        users = User.objects.filter(username__icontains=username_find) \
            .exclude(
                Q(username=current_user.username) |
                Q(pk__in=UserChat.objects.filter(user1=current_user).values_list('user2', flat=True)) |
                Q(pk__in=UserChat.objects.filter(user2=current_user).values_list('user1', flat=True))
            )
        return users.order_by('-username')

    @classmethod
    def create_chat(cls, request: AsgiRequest, username_find: str) -> None:
        current_user = request.user
        interlocutor = User.objects.get(username=username_find)

        if cls.is_chat_exists(current_user, interlocutor):
            raise ChatExistsException
        UserChat.objects.create(user1=current_user, user2=interlocutor)
