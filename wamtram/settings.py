from dbca_utils.utils import env
import os
from pathlib import Path
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = str(Path(__file__).resolve().parents[1])
PROJECT_DIR = str(Path(__file__).resolve().parents[0])
# Add PROJECT_DIR to the system path.
sys.path.insert(0, PROJECT_DIR)

# Settings defined in environment variables.
DEBUG = env('DEBUG', False)
SECRET_KEY = os.environ.get('SECRET_KEY', 'PlaceholderSecretKey')
if not DEBUG:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_DOMAINS', '').split(',')
else:
    ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'wamtram.urls'
WSGI_APPLICATION = 'wamtram.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Application settings
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'turtlesdb',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dbca_utils.middleware.SSOLoginMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'mssql'),
        'HOST': os.environ.get('DB_HOST', 'host'),
        'NAME': os.environ.get('DB_NAME', 'database'),
        'PORT': os.environ.get('DB_PORT', 1234),
        'USER': os.environ.get('DB_USERNAME', 'user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'pass'),
        'OPTIONS': {
            'driver': os.environ.get('DB_DRIVER', 'ODBC Driver 17 for SQL Server'),
            'extra_params': os.environ.get('DB_EXTRA_PARAMS', ''),
        },
    }
}


# Internationalisation.
USE_I18N = False
USE_TZ = True
TIME_ZONE = 'Australia/Perth'
LANGUAGE_CODE = 'en-us'
DATE_INPUT_FORMATS = (
    '%d/%m/%Y',
    '%d/%m/%y',
    '%d-%m-%Y',
    '%d-%m-%y',
    '%d %b %Y',
    '%d %b, %Y',
    '%d %B %Y',
    '%d %B, %Y',
)
DATETIME_INPUT_FORMATS = (
    '%d/%m/%Y %H:%M',
    '%d/%m/%y %H:%M',
    '%d-%m-%Y %H:%M',
    '%d-%m-%y %H:%M',
)

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# Logging settings - log to stdout
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {'format': '%(asctime)s %(levelname)-12s %(name)-12s %(message)s'},
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': sys.stdout,
            'level': 'INFO',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
        'wamtram': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}
