import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from portfolio_app.views import my_portfolio

app_name = 'wildcard'
urlpatterns = [
    path('', my_portfolio, name='wildcard_portfolio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
