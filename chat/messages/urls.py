from django.urls import path
from . import views


app_name = 'messages'

urlpatterns = [
    path('', views.chats, name='chats'),
    path('add_chat/', views.add_chat, name='add_chat'),
    path('add_chat_search/', views.add_chat_search, name='add_chat_search'),
    path('chat/<str:room_name>/', views.dialog, name='room'),
]