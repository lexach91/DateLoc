from django.shortcuts import render


def chat(request, chat_id):
    '''Chat page view'''
    return render(request, "chat/chat.html", {
        'chat_id': chat_id,
    })
