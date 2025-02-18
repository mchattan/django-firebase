from decouple import config, Csv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--ud8wmv8e815a%e*n-mh$_y70uj*!%8r5sjy!%rb8)#14mdr%5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_firebase',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vanilla.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vanilla.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# If running locally, make sure this is set up for additional static dirs
STATICFILES_DIRS = [
    BASE_DIR / "static",  # If you have a global static/ folder
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# FIREBASE
# ----------------------------------------------------------------------------
FCM_PROJECT_ID=config('FCM_PROJECT_ID', '')
FCM_PRIVATE_KEY_ID=config('FCM_PRIVATE_KEY_ID', '').replace('\\n', '\n')
FCM_PRIVATE_KEY=config('FCM_PRIVATE_KEY', '').replace('\\n', '\n')
FCM_CLIENT_ID=config('FCM_CLIENT_ID', '')
FCM_SCOPES=config('FCM_SCOPES', cast=Csv())
FCM_BASE_URL=config('FCM_BASE_URL', 'https://fcm.googleapis.com')
FCM_VAPID_KEY=config('FCM_VAPID_KEY', '')
FCM_API_KEY=config('FCM_API_KEY', '')
FCM_AUTH_DOMAIN=config('FCM_AUTH_DOMAIN', '')
FCM_STORAGE_BUCKET=config('FCM_STORAGE_BUCKET', '')
FCM_APP_ID=config('FCM_APP_ID', '')
FCM_MESSAGING_SENDER_ID=config('FCM_MESSAGING_SENDER_ID', '')
FCM_MEASUREMENT_ID=config('FCM_MEASUREMENT_ID', '')
FCM_DEFAULT_CLICK_DESTINATION=config('FCM_DEFAULT_CLICK_DESTINATION', 'https://www.google.com')
FCM_MESSAGE_ICON=config('FCM_MESSAGE_ICON', '')
FMC_MAX_NOTIFICATIONS_PER_USER=int(config('FMC_MAX_NOTIFICATIONS_PER_USER', 3))