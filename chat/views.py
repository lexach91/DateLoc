from django.shortcuts import render
from .models import PrivateChat, Message


def chat(request, chat_id):
    '''Chat page view'''
    # return render(request, "chat/chat.html", {
    #     'chat_id': chat_id,
    # })
    
    if request.user.is_authenticated:
        chat = PrivateChat.objects.get(id=chat_id)
        if request.user.id == chat.user1.id or request.user.id == chat.user2.id:
            messages = Message.objects.filter(chat=chat)
            return render(request, "chat/chat.html", {
                'chat_id': chat.id,
                'messages': messages,
            })
        else:
            return render(request, "chat/permission_denied.html")
    else:
        return render(request, "chat/permission_denied.html")
