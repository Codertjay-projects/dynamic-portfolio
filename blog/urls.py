from django.urls import path
from .views import (BlogListView,
                    BlogDetailView,
                    update_post_view,
                    DeletePostView,
                    create_comment,
                    BlogCreateView, blog_user_list_view
                    )

app_name = 'blog'
urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('#/<str:username>/', blog_user_list_view, name='blog_user_list'),
    path('#/article_create/', BlogCreateView.as_view(), name='blog_create'),
    path('<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<str:slug>/create_comment/', create_comment, name='blog_comment'),
    path('<str:slug>/update/', update_post_view, name='update_post'),
    path('<str:slug>/delete/', DeletePostView.as_view(), name='delete_post'),
]
