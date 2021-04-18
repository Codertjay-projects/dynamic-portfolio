import os
from decouple import config, Csv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start_date development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third part packages
    'markdown_deux',
    'pagedown',
    'crispy_forms',
    'fontawesome_5',
    'colorful',
    'comments',
    'django.contrib.sites',
    'rest_framework',

    # debug tool bar
    'debug_toolbar',
    # subdomains
    'django_hosts',
    'corsheaders',
    'upload_validator',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    '_profile',
    'home_page',
    'blog',
    'users',
    'portfolio_app',
    'membership',
    'dashboard',

]

MIDDLEWARE = [
    # for django host
    'django_hosts.middleware.HostsRequestMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # for debug toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',

    # for django host
    'django_hosts.middleware.HostsResponseMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home_page.context_processors.add_variable_to_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'Portfolio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'dynamicportfoliodb',
            'USER': 'codertjay',
            'PASSWORD': 'whoamithankgod12dynamicportfolioDB',
            'HOST': 'localhost',
            'PORT': '',
        }

    }

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

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# for django allauth
SITE_ID = 1
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
AUTH_USER_MODEL = 'users.User'
login_url = '/accounts/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SIGNUP_REDIRECT_URL = '/profile/profileUpdate/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# for sending email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)

# this is for django host
ROOT_URLCONF = 'Portfolio.urls'
ROOT_HOSTCONF = "Portfolio.hosts"

if DEBUG:
    PARENT_HOST = '.localhost:8000'
    DEFAULT_HOST = "www"
    DEFAULT_REDIRECT_URL = "http://www.localhost:8000"

else:
    PARENT_HOST = '104.131.111.54:8000'
    DEFAULT_HOST = "www"
    DEFAULT_REDIRECT_URL = "http://104.131.111.54:8000"

# for django debug toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

handler404 = 'portfolio_app.views.handler404'
handler500 = 'portfolio_app.views.handler500'

CORS_ALLOWED_REGEX = config('CORS_ALLOWED_REGEX', cast=Csv())

CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', cast=Csv())

SKIP_PREFLIGHT_CHECK = True

if DEBUG:
    PAYSTACK_LIVE_KEY = "sk_test_ecd835dfbf1a13ca89b9910b920d33d33cdc1a55"
    PAYSTACK_PUBLIC_KEY = "pk_test_618bff50aea7529c52c85adc073a7955fa3c7da1"
else:
    PAYSTACK_LIVE_KEY = "sk_live_7cb2319f4adfbe77b09fd0ef50134c69a2a26761"
    PAYSTACK_PUBLIC_KEY = "pk_live_52c351e9226e7f70fd7913da05159b87bea83522"

