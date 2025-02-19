from django.urls import path
from .views import firebase_test_page, firebase_config, register_web_push
from .views import FirebaseMessagingView, FirebaseMessagingSWView

app_name = 'django_firebase'

urlpatterns = (
    path("firebase/", firebase_test_page, name="index"),
    path("firebase/config/", firebase_config, name="config"),
    path('firebase/register-web-push/', register_web_push, name='register_web_push'),
    path("firebase-messaging-sw.js", FirebaseMessagingSWView.as_view(), name="firebase-messaging-sw"),
    path("django-firebase.js", FirebaseMessagingView.as_view(), name="firebase-messaging"),
)