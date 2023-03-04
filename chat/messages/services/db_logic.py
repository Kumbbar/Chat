from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.db.models import Q

from dataclasses import dataclass

from .exceptions import ChatExistsException
from ..models import UserChat, Message, MessageStatus


@dataclass
class MessageStatusConsts:
    UNREAD: str = "не прочитано"
    READ: str = "прочитано"


class UserChatsService:
    @classmethod
    def is_chat_exists(cls, current_user: User, interlocutor: User) -> bool:
        return True if UserChat.objects.filter(
            Q(user1=current_user, user2=interlocutor) |
            Q(user2=current_user, user1=interlocutor)
        ).first() or current_user == interlocutor else False

    @classmethod
    def get_user_chats(cls, user: User) -> QuerySet:
        # No user input
        chats = UserChat.objects.raw(
            '''
                SELECT 
                user_chats.id as id, 
                CASE 
                    WHEN user_chats.user1_id = %(current_user)s THEN auth_user2.username
                    WHEN user_chats.user2_id = %(current_user)s THEN auth_user1.username
                END as interlocutor,
                (
                    SELECT COUNT(*)
                    FROM messages 
                    JOIN message_statuses ON messages.message_status_id = message_statuses.id
                    WHERE messages.chat_id = user_chats.id
                    AND messages.user_receiver_id = %(current_user)s
                    AND message_statuses.name = '%(unread_status)s'
                ) as unread_messages
                FROM user_chats 
                JOIN auth_user auth_user1 ON user_chats.user1_id = auth_user1.id
                JOIN auth_user auth_user2 ON user_chats.user2_id = auth_user2.id
                WHERE user_chats.user1_id = %(current_user)s
                OR user_chats.user2_id = %(current_user)s
            ''' % {'current_user': user.pk, 'unread_status': MessageStatusConsts.UNREAD}
        )
        return chats

    @classmethod
    def get_chat(cls, current_user: User, interlocutor: User):
        return UserChat.objects.get(
                Q(user1=current_user, user2=interlocutor) |
                Q(user2=current_user, user1=interlocutor)
        )

    @classmethod
    def get_users_without_chat(cls, current_user: User, username_find: str) -> QuerySet[User]:
        users = User.objects.filter(username__icontains=username_find) \
            .exclude(
            Q(username=current_user.username) |
            Q(pk__in=UserChat.objects.filter(user1=current_user).values_list('user2', flat=True)) |
            Q(pk__in=UserChat.objects.filter(user2=current_user).values_list('user1', flat=True))
        ).order_by('-username')
        return users

    @classmethod
    def create_chat(cls, current_user: User, username_find: str) -> None:
        interlocutor = User.objects.get(username=username_find)

        if cls.is_chat_exists(current_user, interlocutor):
            raise ChatExistsException
        UserChat.objects.create(user1=current_user, user2=interlocutor)


class MessageService:
    @classmethod
    def create_message_by_usernames(cls, message: str, sender: str, receiver: str) -> None:
        sender = User.objects.get(username=sender)
        receiver = User.objects.get(username=receiver)
        if UserChatsService.is_chat_exists(sender, receiver):
            Message.objects.create(
                text=message,
                user_sender=sender,
                user_receiver=receiver,
                message_status=MessageStatus.objects.get(name=MessageStatusConsts.UNREAD),
                chat=UserChatsService.get_chat(sender, receiver)
            )

    @classmethod
    def get_chat_messages(cls, current_user: User, interlocutor: str) -> QuerySet:
        messages = Message.objects.select_related('user_sender', 'user_receiver').filter(
            Q(user_sender=current_user, user_receiver__username=interlocutor) |
            Q(user_sender__username=interlocutor, user_receiver=current_user)
        ).order_by('-created_at')
        return messages

    @classmethod
    def get_and_read_chat_messages(cls, current_user: User, interlocutor: str) -> QuerySet:
        messages = cls.get_chat_messages(current_user, interlocutor)
        received_messages = messages.filter(user_receiver=current_user)
        read_status = MessageStatus.objects.get(name=MessageStatusConsts.READ)

        for message in received_messages:
            message.message_status = read_status
        Message.objects.bulk_update(received_messages, fields=['message_status'])
        return messages
