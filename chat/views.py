from django.shortcuts import render
from .models import PrivateChat, Message


def chat(request, chat_id):
    '''Chat page view'''
    if not request.user.is_authenticated:
        return render(request, "chat/permission_denied.html")
    chat = PrivateChat.objects.get(id=chat_id)
    if request.user.id not in [chat.user1.id, chat.user2.id]:
        return render(request, "chat/permission_denied.html")
    messages = Message.objects.filter(chat=chat)
    return render(request, "chat/chat.html", {
        'chat_id': chat.id,
        'messages': messages,
    })
