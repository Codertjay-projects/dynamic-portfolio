from decouple import config

# Todo change database
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRESQL_DATABASE_NAME'),
        'USER': config('POSTGRESQL_DATABASE_USER'),
        'PASSWORD': config('POSTGRESQL_DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
PARENT_HOST = '104.131.111.54:8000'
DEFAULT_HOST = "www"
DEFAULT_REDIRECT_URL = "http://104.131.111.54:8000"

PAYSTACK_LIVE_KEY = config('PAYSTACK_LIVE_KEY', default='')
PAYSTACK_PUBLIC_KEY = config('PAYSTACK_PUBLIC_KEY', default='')
