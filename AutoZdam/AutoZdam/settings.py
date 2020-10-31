

import os
import django_heroku
import dj_database_url
from decouple import config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b%-@#v^-wu(1-)fi_!5p!4zl-)zmho5^6w1#lz0cy3sedhydid'

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
    'Auto_Zdam',
    'widget_tweaks',
    'django_filters'


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',


]

ROOT_URLCONF = 'AutoZdam.urls'


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

WSGI_APPLICATION = 'AutoZdam.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'HOST': '127.0.0.1',
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'auto_zdam',
#        'USER': 'postgres',
#        'PASSWORD': 'coderslab',
#    }
#}

DATABASES = {
    'default': {
        'HOST': 'ec2-52-73-199-211.compute-1.amazonaws.com',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'davi8n4js8730v',
        'USER': 'guwiafjszdajmc',
        'PASSWORD': 'e8307bea4b978b54f79b007eae01c028d0944b5ffaf9a028d7c57eba2ac3a016',
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# User substitution
# https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#auth-custom-user

AUTH_USER_MODEL = 'Auto_Zdam.User'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    '/var/www/static/',
#]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_HOST = 'poczta.o2.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'swierad-88@o2.pl'
EMAIL_HOST_PASSWORD = 'umbridge'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

django_heroku.settings(locals())