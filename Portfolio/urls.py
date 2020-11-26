from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog.views import BlogCreateView


urlpatterns = [
    path('administrator/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', include('_profile.urls')),
    path('user/', include('users.urls')),
    path('url/', include('single_url.urls')),
    path('blog/', include('blog.urls')),
    path('', include('portfolio_app.urls'),name='portfolio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
