from django.urls import path
from blog.views import BlogCreateView

app_name = 'single_url'

urlpatterns = [
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
]
