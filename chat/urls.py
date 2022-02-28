from django.urls import path
from . import views

urlpatterns = [
    path('<int:chat_id>/', views.chat, name="chat"),
    path('save_message/<int:chat_id>/', views.save_message, name="save_message"),
    path('get_or_create_chat/<str:user2>', views.get_or_create_chat, name="get_or_create_chat"),
]
