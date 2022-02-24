from django.shortcuts import render


def chat(request):
    '''Chat page view'''
    return render(request, "chat/chat.html")
