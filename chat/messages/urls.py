from django.urls import path
from . import views
from . import api_views
app_name = 'messages'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    # path('api', api_views.get_messages, name='api')
]