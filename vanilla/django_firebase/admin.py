from django.contrib import admin
from .models import FCMUserToken

@admin.register(FCMUserToken)
class FCMUserTokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'type', 'last_updated', 'token']
    readonly_fields = ['created', 'last_updated']