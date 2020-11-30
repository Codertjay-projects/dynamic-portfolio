import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start_date development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1py)l9&2-f%omx17p^e8m8sf1^dtr=5-9d4+178p#1c(f35m)%'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

CSRF_COOKIE_DOMAIN = '.localhost:8000'

if DEBUG == True:
    ALLOWED_HOSTS = ['.localhost', 'localhost']

else:
    ALLOWED_HOSTS = ['']

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

    'blog',
    'project',
    'users',
    'portfolio_app',
    'single_url',

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
                'blog.context_processors.add_variable_to_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'Portfolio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
STATIC_ROOT = os.path.join(BASE_DIR, 'portfolio_app/static')

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
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'dynamicportfl@gmail.com'
EMAIL_HOST_PASSWORD = 'wh0@m1dyn@m1cp0rtftl'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# this is for django host
ROOT_URLCONF = 'Portfolio.urls'
ROOT_HOSTCONF = "Portfolio.hosts"
PARENT_HOST = '.localhost:8000'
DEFAULT_HOST = "www"

DEFAULT_REDIRECT_URL = "http://www.localhost:8000"

# for django debug toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

handler404 = 'portfolio_app.views.handler404'
handler500 = 'portfolio_app.views.handler500'

CORS_ALLOWED_ORIGINS = [
    'https://www.localhost:8000',
    'https://.localhost:8000',
    'http://codertjay.localhost:8000',
]

CORS_ALLOWED_REGEX = [
    r"^http://\w+\.localhost\:8000$",
    # for subdomain
    r"^http://\w+\.example\.com$",
    r"^http://\w+\.localhost:8000$",
    r"^https://codertjay.localhost$",
]
