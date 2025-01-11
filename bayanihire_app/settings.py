"""
Django settings for bayaniHire_prelims project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1y5$^!t!eyrq0u15amq)5_y3ga*(37bvz38y1n4=@di(x00uw='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['WeinJazfer.pythonanywhere.com']  # Add your allowed hosts here

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'bayanihire_app',  # Your app
    'users_app',      # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'users_app.middleware.NoCacheMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'users_app' / 'templates'],
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

ROOT_URLCONF = 'bayanihire_app.urls'
WSGI_APPLICATION = 'bayanihire_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'WeinJazfer$default',  # Replace with your database name
        'USER': 'WeinJazfer',  # Replace with your database user
        'PASSWORD': 'Marito1234',  # Replace with your database password
        'HOST': 'WeinJazfer.mysql.pythonanywhere-services.com',
        'PORT': '3306',  # Replace with your database port if needed
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
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Use the Path '/' operator for joining paths

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Define this if your application handles media files

# Additional locations of static files
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Assumed that you manually manage some static files here
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email Function
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'automatedbayanihire@gmail.com'
EMAIL_HOST_PASSWORD = 'ddgp irir jfxq tkdq'
DEFAULT_FROM_EMAIL = 'automatedbayanihire@gmail.com'
SITE_ID = 1

# Session Configuration
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Store sessions in the database
SESSION_COOKIE_AGE = 1800  # Session valid for 30 minutes (in seconds)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep session alive even after closing the browser
SESSION_SAVE_EVERY_REQUEST = True  # Reset session expiry on each request
BASE_URL = "WeinJazfer.pythonanywhere.com"  # Replace with your actual domain in production

DATA_UPLOAD_MAX_MEMORY_SIZE = 64 * 1024 * 1024  # 64MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 64 * 1024 * 1024  # 64MB

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
