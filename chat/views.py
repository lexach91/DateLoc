from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import PrivateChat, Message
from django.contrib.auth.models import User


def chat(request, chat_id):
    '''Chat page view'''
    if not request.user.is_authenticated:
        return render(request, "chat/permission_denied.html")
    chat_obj = get_object_or_404(PrivateChat, pk=chat_id)    
    if request.user.id not in [chat_obj.user1.id, chat_obj.user2.id]:
        return render(request, "chat/permission_denied.html")
    messages = chat_obj.messages.all().order_by("date")
    return render(request, "chat/chat.html", {
        'chat_id': chat_obj.id,
        'messages': messages,
    })
    
    
def save_message(request, chat_id):
    '''Save message to database'''
    if request.is_ajax():
        chat_obj = get_object_or_404(PrivateChat, pk=chat_id)
        if request.user.id not in [chat_obj.user1.id, chat_obj.user2.id]:
            return JsonResponse({'error': 'You are not allowed to send messages to this chat'})
        message = request.POST.get("message")
        # user_id = request.POST.get("user_id")
        # user = get_object_or_404(User, pk=user_id)
        if message:
            Message.objects.create(chat=chat_obj, sender=request.user, message=message)
            message = Message.objects.filter(chat=chat_obj, sender=request.user).order_by("-date")[0]
            return JsonResponse({'message': message.message, 'date': message.date.strftime("%b. %d, %Y, %I:%M %p")})
        
def get_or_create_chat(request, user2):
    '''Get or create chat between two users'''
    user2 = get_object_or_404(User, pk=user2)
    chat_obj = PrivateChat.objects.get_or_create(user1=request.user, user2=user2)[0]
    chat_obj.save()
    return HttpResponseRedirect(f'/chat/{chat_obj.id}/')
