"""
Django settings for motherapp project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2=s177hyr-mu^wp)1dc43j%^ek=zbf&e4=cd+j8^bjxw!h5fs%'
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '2=s177hyr-mu^wp)1dc43j%^ek=zbf&e4=cd+j8^bjxw!h5fs%')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = []

#SESSION_COOKIE_SECURE = True

#SECURE_SSL_REDIRECT = True

#CSRF_COOKIE_SECURE = True

#SECURE_HSTS_SECONDS = 3

#SECURE_HSTS_PRELOAD = True

#SECURE_HSTS_INCLUDE_SUBDOMAINS = True

#USE_L10N = True

#USE_THOUSAND_SEPARATOR = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'michijapp',
    'jackhun',
    'django_countries',
    'djrichtextfield',
    'cart'
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

DJRICHTEXTFIELD_CONFIG ={
    'js': ['//cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js'],
    'init_template': 'djrichtextfield/init/tinymce.js',
    'settings':{
        'menubar' : False,
        'plugins' : 'link image',
        'toolbar' : 'bold italic underline | link image | removeformat',
        'width' : 700
    }
}

CART_SESSION_ID = 'cart'

ROOT_URLCONF = 'motherapp.urls'

#X_FRAME_OPTIONS = 'DENY'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'motherapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# The static dir is where django will also look for static files to serve in the app
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
    #'/var/www/staticfiles',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = 'michijltd247@gmail.com'

EMAIL_HOST_NAME = 'Michael_Oforkansi'

EMAIL_HOST_PASSWAORD = 'Sightman99'

EMAIL_PORT = 587

EMAIL_USE_TLS = True
