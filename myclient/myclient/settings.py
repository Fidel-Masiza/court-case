"""
Django settings for myclient project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-)rpq4jvhujouna8(je@+r_6n3#$uv@ezky@6f38t%!^f0od#9o'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True # Ensure this is set to False in production
import os
# Set allowed hosts for development

ALLOWED_HOSTS = ['127.0.0.1', 'localhost','*' ,'cout-order.onrender.com']

# Set the SITE_URL based on the DEBUG value
if DEBUG:
    SITE_URL = 'http://127.0.0.1:8000'
else:
    SITE_URL = 'https://cout-order.onrender.com'

print(f'DEBUG is set to {DEBUG}. Site URL is set to {SITE_URL}')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  
    'mytrial',
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

ROOT_URLCONF = 'myclient.urls'

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

WSGI_APPLICATION = 'myclient.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'fidelmasitsa03@gmail.com'  
EMAIL_HOST_PASSWORD = 'qkhq cenh zirv qonj'  
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


CENTRAL_NOTIFICATION_EMAIL = 'betsuccor@gmail.com'  



ADMIN_EMAILS = [
    'goergew424@gmail.com',
    'admin2@example.com',
    'admin3@example.com',
    'admin4@example.com',
    'admin5@example.com',
]


PAYPAL_CLIENT_ID = 'AbtkUk0TVy-hfNj1EZG9mkwh5K4nHC_QeifnvJQp2v7EYe0fLq_sn2vy3bHbeGtzAvjVCG0TByt-zChw'
PAYPAL_CLIENT_SECRET ='EMVx7n8euV3m9Hpe0uyga0dQy_VevaUuDff8wQt0zUCQIDO4rGwDEVU4sVlJQGxffCKaF5WZdBhaerKL'
PAYPAL_MODE = 'live'  # or 'live' for production what is this paypal_mode? if i only have these  App name
