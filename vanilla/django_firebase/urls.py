from django.urls import path
from .views import firebase_test_page, firebase_config, register_web_push
from .views import FirebaseMessagingView, FirebaseMessagingSWView
# from django.views.generic import TemplateView
# from django.conf import settings


app_name = 'django_firebase'

# FIREBASE_CONFIG = {
#     'apiKey': settings.FCM_API_KEY,
#     'authDomain': settings.FCM_AUTH_DOMAIN,
#     'projectId': settings.FCM_PROJECT_ID,
#     'storageBucket': settings.FCM_STORAGE_BUCKET,
#     'messagingSenderId': settings.FCM_MESSAGING_SENDER_ID,
#     'appId': settings.FCM_APP_ID,
#     'vapidKey': settings.FCM_VAPID_KEY,
# }

urlpatterns = (
    path("firebase/", firebase_test_page, name="index"),
    path("firebase/config/", firebase_config, name="config"),
    path('firebase/register-web-push/', register_web_push, name='register_web_push'),
    path("firebase-messaging-sw.js", FirebaseMessagingSWView.as_view(), name="firebase-messaging-sw"),
    path("django-firebase.js", FirebaseMessagingView.as_view(), name="firebase-messaging"),

    # path("firebase-messaging-sw.js", TemplateView.as_view(
    #     extra_context=FIREBASE_CONFIG,
    #     template_name="django_firebase/firebase-messaging-sw.js",
    #     content_type="application/javascript")
    #  ),

)