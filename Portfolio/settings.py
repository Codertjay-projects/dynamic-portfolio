import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start_date development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1py)l9&2-f%omx17p^e8m8sf1^dtr=5-9d4+178p#1c(f35m)%'

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

    'markdown_deux',
    'pagedown',
    'crispy_forms',
    'fontawesome_5',
    'colorful',
    'comments',
    'django.contrib.sites',
    'rest_framework',

    # subdomains
    # 'django_hosts',
    # 'subdomains ',

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
    # 'django_hosts.middleware.HostsRequestMiddleware',

    'subdomains.middleware.SubdomainURLRoutingMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'django_hosts.middleware.HostsResponseMiddleware'
]

ROOT_URLCONF = 'Portfolio.urls'

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

CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD =config('EMAIL_HOST_PASSWORD')


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'portfolio_app/static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
SITE_ID = 1

ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'
AUTH_USER_MODEL = 'users.User'

login_url = '/accounts/login'
LOGIN_REDIRECT_URL = '/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'favourtjai@gmail.com'
EMAIL_HOST_PASSWORD = 'thankgod12'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# ROOT_URLCONF = 'Portfolio.urls.portfolio'

# ROOT_HOSTCONF = "portfolio.com"


# This is the urlconf that will be used for any subdomain that is not
# listed in ``SUBDOMAIN_URLCONFS``, or if the HTTP ``Host`` header does not
# contain the correct domain.
# If you're planning on using wildcard subdomains, this should correspond
# to the urlconf that will be used for the wildcard subdomain. For example,
# 'accountname.mysite.com' will load the ROOT_URLCONF, since it is not
# defined in ``SUBDOMAIN_URLCONFS``.


# A dictionary of urlconf module paths, keyed by their subdomain.
# SUBDOMAIN_URLCONFS = {
#     None: 'myproject.urls.frontend',  # no subdomain, e.g. ``example.com``
#     'www': 'myproject.urls.frontend',
# }
