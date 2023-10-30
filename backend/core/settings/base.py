import os
from pathlib import Path

from decouple import config
from django.utils.translation import gettext_lazy

from .cors import *
from .jazzmin import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY
SECRET_KEY = config('SECRET_KEY')

# DEBUG
DEBUG = config('DEBUG', default=False, cast=bool)

# defining the project state
PRODUCTION = config('PRODUCTION', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS').split(',')


INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# Application definition
THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'drf_spectacular',
    'django_admin_logs',
]

if not PRODUCTION:
    THIRD_PARTY_APPS += [
        'debug_toolbar'
    ]

ADMIN_APPS = [
    'jazzmin',
    'modeltranslation',
]

LOCAL_APPS = [

]

INSTALLED_APPS = [
    *ADMIN_APPS,

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
    'django_cleanup',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware', # activate only during development
    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'

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

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# LANGUAGES = (
#     ('ru', gettext_lazy('Russian')),
#     ('en', gettext_lazy('English')),
#     ('ky', gettext_lazy('Kyrgyz')),
# )

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# if DEBUG:
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static_back/')
#     ]

STATIC_URL = 'static_back/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

MEDIA_URL = '/media_storage/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_storage/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT')
    }
}

# Admin site customization

DJANGO_ADMIN_LOGS_ENABLED = False

REST_FRAMEWORK = {

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USE_SSL = config('EMAIL_USE_SSL')