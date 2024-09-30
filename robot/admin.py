from django.contrib import admin
from .models import TelegramUser


class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ['full_name','username','user_id',]
    search_fields = ['full_name','username','user_id']

admin.site.register(TelegramUser, TelegramUserAdmin)
