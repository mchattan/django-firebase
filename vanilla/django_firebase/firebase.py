from django.conf import settings
from google.auth import credentials
from .models import FCMUserToken, FCMTokenType
import firebase_admin
from firebase_admin import credentials, messaging

# REGISTER FIREBASE
credentials_dict = {
    "type": f"service_account",
    "project_id": f'{settings.FCM_PROJECT_ID}',
    "private_key_id": f'{settings.FCM_PRIVATE_KEY_ID}',
    "private_key": f'{settings.FCM_PRIVATE_KEY}',
    "client_email": f"firebase-adminsdk-fbsvc@{settings.FCM_PROJECT_ID}.iam.gserviceaccount.com",
    "client_id": f'{settings.FCM_CLIENT_ID}',
    "auth_uri": f"https://accounts.google.com/o/oauth2/auth",
    "token_uri": f"https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40{settings.FCM_PROJECT_ID}.iam.gserviceaccount.com",
    "universe_domain": f"googleapis.com"
}
cred = credentials.Certificate(credentials_dict)
firebase_admin.initialize_app(cred)

print(firebase_admin._apps)

class FirebaseQuickTest:


    def send_test_message(self, token):  # Simplified for testing

        message = messaging.Message(
            token=token,
            data={
                'title': 'Firebase Test Title!',
                'body': 'Firebase message, https://www.google.com',
                'image': settings.FCM_MESSAGE_ICON,
                'click_action': 'https://www.google.com'
            }
        )
        try:
            response = messaging.send(message)
            print(f"Successfully sent message: {response}")
        except messaging.exceptions.FirebaseError as e:
            print(f"Error sending message: {e}")


class FirebaseTool:

    def send_web_notification(self, user, title, body, url):
        """Send HTTP request to FCM with given message.

          Args:
            fcm_message: JSON object that will make up the body of the request.
        """
        user_tokens = FCMUserToken.objects.filter(user=user, type=FCMTokenType.WEB).order_by('-last_updated')
        for utk in user_tokens[:settings.FMC_MAX_NOTIFICATIONS_PER_USER]:
            # limit notification to last n registered devices per user
            self.send_fcm_message(body, title, utk.token, url)


    def send_fcm_message(self, body, title, token, url=None):
        url = url if url else settings.FCM_DEFAULT_CLICK_DESTINATION
        try:
            message = messaging.Message(
                token=token,
                data={
                    'title': title,
                    'body': body,
                    'image': settings.FCM_MESSAGE_ICON,
                    'click_action': url
                }
            )
            response = messaging.send(message)
            print(f"Successfully sent message: {response}")
        except messaging.exceptions.FirebaseError as e:
            print(f"Error sending message: {e}")



