from django.urls import path
from . import views


app_name = 'messages'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_chat/', views.add_chat, name='add_chat'),
    path('chat/<str:room_name>/', views.dialog, name='room'),
]