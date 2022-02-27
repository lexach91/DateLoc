from django.contrib import admin
from .models import PrivateChat, Message

# Register your models here.
@admin.register(PrivateChat)
class PrivateChatAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('user1', 'user2', )
    list_display = ('user1', 'user2')
    search_fields = ['user1', 'user2']
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('chat', 'sender', )
    list_display = ('chat', 'sender', 'message', 'date')
    search_fields = ['chat', 'sender']