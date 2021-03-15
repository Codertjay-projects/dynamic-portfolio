from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
import debug_toolbar

from portfolio_app.views import my_portfolio

urlpatterns = [
    path('administrator/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('allauth.urls')),
    # path('dashboard/', include('_profile.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('user/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('payment/', include('membership.urls')),
    path('', include('home_page.urls')),
    path('#/', include('portfolio_app.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
