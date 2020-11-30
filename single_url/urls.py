from django.urls import path
from blog.views import BlogCreateView
from portfolio_app.views import about_view, contact_view

app_name = 'single_url'

urlpatterns = [
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]
