from django.conf import settings
from django_hosts import patterns, host

from portfolio_app.views import my_portfolio

host_patterns = patterns(
    '',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host('', settings.ROOT_URLCONF, name=''),
    host(r'(?P<username>\w+)', 'Portfolio.hostsconf.urls',
         callback=my_portfolio, name='with-callback'),
)
