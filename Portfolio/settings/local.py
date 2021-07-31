from .base import *
from decouple import config, Csv
print('using local')
DEBUG = True
SECRET_KEY = config('DEBUG_SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

PARENT_HOST = '.localhost:8000'
DEFAULT_HOST = "www"
DEFAULT_REDIRECT_URL = "http://www.localhost:8000"

# for django debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'thankgod12',
        'HOST': 'localhost',
        'PORT': '',
    }
}

PAYSTACK_LIVE_KEY = config('PAYSTACK_DEBUG_LIVE_KEY', default='')
PAYSTACK_PUBLIC_KEY = config('PAYSTACK_DEBUG_PUBLIC_KEY', default='')
