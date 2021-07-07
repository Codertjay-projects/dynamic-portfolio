# Application definition
LOCAL_APPS = [

    '_profile',
    'home_page',
    'blog',
    'users',
    'portfolio_app',
    'membership',
    'dashboard',

]
THIRD_PARTY_APPS = [

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

]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += THIRD_PARTY_APPS
