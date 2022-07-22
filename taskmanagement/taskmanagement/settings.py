"""
Django settings for taskmanagement project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from taskmanagement.config import Config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEFAULT_PORT = Config.DEFAULT_PORT
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--_t)&hwjzixaj$$83hve-$ck0ab=#ohre4_5@$g7d=#39@egwo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = Config.DEBUG

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user_auth',
    'projects',
    'tasks',
    'notes',
    'comments',
    'tags',
    'rest_framework',
    'rest_framework_swagger',
    'drf_yasg',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'django_jwt_extended'
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

ROOT_URLCONF = 'taskmanagement.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'taskmanagement.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': Config.DB_NAME,
        'USER': Config.DB_USER,
        'PASSWORD': Config.DB_PASSWORD,
        'HOST': Config.DB_HOST,
        'PORT': Config.DB_PORT,
    }
}

# DATABASES = {

# 'default': {

# 'ENGINE': 'django.db.backends.postgresql',

# 'NAME': 'akash_kareliya',

# 'USER': 'akash_kareliya',

# 'PASSWORD': 'deep70',

# 'HOST': 'localhost',

# 'PORT': '',

# }

# }
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static/'),]
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'anirudhflutter@gmail.com'
EMAIL_HOST_PASSWORD = 'yxhyhxbnrqstyaek'

REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
                  'DEFAULT_PERMISSION_CLASSES': (
                      # 'rest_framework.permissions.IsAdminUser',
                  ),
                  'DEFAULT_AUTHENTICATION_CLASSES': (
                      'rest_framework.authentication.TokenAuthentication',
                      'rest_framework.authentication.BasicAuthentication',
                      'rest_framework.authentication.SessionAuthentication',
                  )
                  }

# JWT settings
JWT_TOKEN_EXPIRY = 7   # No. of days
JWT_ALGORITHM = 'HS256'  # Algorithm specified by JWT
JWT_UTF = 'utf-8'

