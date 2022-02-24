from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Filters, displays and search for django admin"""
    list_filter = ('display_name', 'town_or_city', 'county', 'user', )
    list_display = ('display_name', 'bio', 'image', 'job_title', 'phone_number', 'town_or_city', 'county', 'user')
    search_fields = ['display_name', 'town_or_city', 'county', 'user']
