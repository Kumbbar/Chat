from django.urls import path
from . import views


app_name = 'messages'

urlpatterns = [
    path('', views.chats, name='chats'),
    path('add/', views.add_chat_page, name='add_chat_page'),
    path('add/<str:username>/', views.add_chat, name='add_chat'),
    path('add_search/', views.add_chat_search, name='add_chat_search'),
    path('<str:room_name>/', views.dialog, name='room'),
]