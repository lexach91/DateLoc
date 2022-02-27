from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import PrivateChat, Message


def chat(request, chat_id):
    '''Chat page view'''
    if not request.user.is_authenticated:
        return render(request, "chat/permission_denied.html")
    chat = get_object_or_404(PrivateChat, pk=chat_id)    
    if request.user.id not in [chat.user1.id, chat.user2.id]:
        return render(request, "chat/permission_denied.html")
    messages = chat.messages.all().order_by("date")
    return render(request, "chat/chat.html", {
        'chat_id': chat.id,
        'messages': messages,
    })
    
    
def save_message(request, chat_id):
    '''Save message to database'''
    if request.is_ajax() and request.user.is_authenticated:
        chat = get_object_or_404(PrivateChat, pk=chat_id)
        if request.user.id not in [chat.user1.id, chat.user2.id]:
            return JsonResponse({'error': 'You are not allowed to send messages to this chat'})
        message = request.POST.get("message")
        sender = request.user
        if message:
            Message.objects.create(chat=chat, sender=sender, message=message)
            message = Message.objects.filter(chat=chat, sender=sender).order_by("-date")[0]
            return JsonResponse({'message': message.message, 'date': message.date.strftime("%b. %d, %Y, %I:%M %p"), 'sender': message.sender.username})