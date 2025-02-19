from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import FCMUserToken
from .forms import FCMTokenUpdateForm
from django.shortcuts import render
from django.views.generic import TemplateView
import json

FIREBASE_CONFIG = {
    'apiKey': settings.FCM_API_KEY,
    'authDomain': settings.FCM_AUTH_DOMAIN,
    'projectId': settings.FCM_PROJECT_ID,
    'storageBucket': settings.FCM_STORAGE_BUCKET,
    'messagingSenderId': settings.FCM_MESSAGING_SENDER_ID,
    'appId': settings.FCM_APP_ID,
    'vapidKey': settings.FCM_VAPID_KEY,
}

@login_required
def firebase_test_page(request):
    context = {
        "firebase_config": FIREBASE_CONFIG
    }
    return render(request, template_name="django_firebase/index.html", context=context)


@login_required
def firebase_config(request):
    return JsonResponse(FIREBASE_CONFIG)


@login_required
def register_web_push(request):
    """Register FCM Web Push subscription"""
    form = FCMTokenUpdateForm(request.POST)
    if form.is_valid():
        user = request.user
        previous_token = form.cleaned_data.get("previous_token")
        new_token = form.cleaned_data["new_token"]
        # print(f'{previous_token=}, {new_token=}')

        if (fcm_token := FCMUserToken.objects.filter(user=user, token=previous_token).first()):
            fcm_token.token = new_token
            fcm_token.save()
            return JsonResponse({"message": "FCM token updated successfully."})
        else:
            FCMUserToken.objects.create(user=user, token=new_token)
            return JsonResponse({"message": "FCM token created successfully."})

    return JsonResponse({"error": form.errors}, status=400)


class FirebaseMessagingView(TemplateView):
    template_name = "django_firebase/django-firebase.js"
    content_type = "application/javascript"
    extra_context = FIREBASE_CONFIG


class FirebaseMessagingSWView(TemplateView):
    template_name = "django_firebase/firebase-messaging-sw.js"
    content_type = "application/javascript"
    extra_context = FIREBASE_CONFIG