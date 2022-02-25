from django.contrib import admin
from .models import Location_Match


@admin.register(Location_Match)
class Location_MatchAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('match', 'user_profile', 'location', 'user', )
    list_display = ('user_profile', 'location', 'user')
    search_fields = ['match', 'user_profile', 'location', 'user']
