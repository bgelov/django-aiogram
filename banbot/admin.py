from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Chat, User


class ChatAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('chat_id', 'title')
admin.site.register(Chat, ChatAdmin)

class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('chat_id', 'first_name', 'last_name', 'username', 'can_basta', 'can_ban', 'can_ban_all', 'can_mute', 'can_mute_all')
    list_editable = ['can_basta', 'can_ban', 'can_ban_all', 'can_mute', 'can_mute_all']
admin.site.register(User, UserAdmin)

class MemberAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('chat_id', 'first_name', 'last_name', 'username')
admin.site.register(User, UserAdmin)
