from django.urls import path
from .views import firebase_test_page, firebase_config, register_web_push
from django.views.generic import TemplateView

app_name = 'django_firebase'


urlpatterns = (
    path("", firebase_test_page, name="index"),
    path("config/", firebase_config, name="config"),
    path('register-web-push/', register_web_push, name='register_web_push'),
    # path("firebase-messaging-sw.js", TemplateView.as_view(
    #         template_name="django_firebase/firebase-messaging-sw.js",
    #         content_type="application/javascript")
    #  ),
)