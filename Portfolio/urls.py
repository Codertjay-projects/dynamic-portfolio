import debug_toolbar
from decouple import config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from blog.views import ArticleSitemap, UserArticleSitemap
from home_page.views import AdsView, StaticSitemap, BingXmlView

sitemaps = {
    'blog': ArticleSitemap,
    'static': StaticSitemap,
    'user_post': UserArticleSitemap,
}

urlpatterns = [
    path('ads.txt', AdsView.as_view()),
    path('BingSiteAuth.xml', BingXmlView.as_view()),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('', include('_profile.urls')),
    path('', include('skill.urls')),
    path('', include('service.urls')),
    path('', include('resume.urls')),
    path('', include('project.urls')),
    path('', include('testimonial.urls')),
    path('', include('pagedown.urls')),
    path('dashboard/', include('dashboard.urls')),

    path(f"{config('ADMIN_URL')}/", admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('accounts/', include('allauth.urls')),

    path('user/', include('users.urls')),
    path('blog/', include('blog.urls')),
    path('payment/', include('membership.urls')),
    path('', include('home_page.urls')),
    path('#/', include('portfolio_app.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
