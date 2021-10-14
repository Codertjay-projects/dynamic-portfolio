from .base import *

print('using local')
DEBUG = True

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRESQL_DATABASE_NAME'),
        'USER': config('POSTGRESQL_DATABASE_USER'),
        'PASSWORD': config('POSTGRESQL_DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}
PAYSTACK_LIVE_KEY = config('PAYSTACK_DEBUG_LIVE_KEY', default='')
PAYSTACK_PUBLIC_KEY = config('PAYSTACK_DEBUG_PUBLIC_KEY', default='')

PARENT_HOST = '.localhost:8000'
DEFAULT_HOST = "www"
DEFAULT_REDIRECT_URL = "http://www.localhost:8000"


