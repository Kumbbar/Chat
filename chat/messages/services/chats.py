from channels.http import AsgiRequest
from django.contrib.auth.models import User
from ..models import UserChat


class UsersChatsService:
    @staticmethod
    def get_users_without_chat(request: AsgiRequest, username_find: str):
        current_user = User.objects.get(username=request.user.username)
        users = User.objects.filter(username__icontains=username_find) \
            .exclude(username=current_user.username) \
            .exclude(pk__in=UserChat.objects.filter(user1=current_user).values_list('user2', flat=True)) \
            .exclude(pk__in=UserChat.objects.filter(user2=current_user).values_list('user1', flat=True))
        return users.order_by('-username')