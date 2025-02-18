from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FCMTokenType(models.TextChoices):
    WEB = 'WEB', 'Web',
    IOS = 'IOS', 'iOS'
    ANDROID = 'ANDROID', 'Android'
    SMS = 'SMS', 'SMS'

class FCMUserToken(models.Model):
    user = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=32, blank=False, null=False,
                            choices=FCMTokenType.choices, default=FCMTokenType.WEB)
    token = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = 'FCM User Token'
        verbose_name_plural = 'FCM User Tokens'