from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django_firebase.models import FCMUserToken
from django_firebase.firebase import FirebaseQuickTest, FirebaseTool
User = get_user_model()


class Command(BaseCommand):
    """
    This CM will send a test notification

    """

    def add_arguments(self, parser):
        parser.add_argument('-pk', '--user_pk', type=int, default=1)
        # parser.add_argument('-lid', '--load_id', type=int, default=1)1
        # parser.add_argument('-c', '--count', type=int, default=1)

    def handle(self, *args, **kwargs):

        print('Test Firebase Notifications')

        qb = FirebaseQuickTest()
        ft = FirebaseTool()


        user_pk = kwargs.get('user_pk', 1)
        user = User.objects.filter(pk=user_pk).first()
        if user:
            fcm_user_tokens = FCMUserToken.objects.filter(user=user)
            for fcm_user_token in fcm_user_tokens:
                # print(f'{user=} {fcm_user_token.token=}')
                # qb.send_test_message(token=fcm_user_token.token)
                ft.send_web_notification(user=user, title='Standard Test Title', body='Standard message body here, http://somewhere.com',
                                         url='https://www.google.com')


