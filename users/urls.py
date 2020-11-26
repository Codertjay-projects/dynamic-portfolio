from django.urls import path
from .views import ContactUserView, contactAdminView



app_name = 'user'
urlpatterns = [
    path('contactuser/', ContactUserView.as_view(), name='contact_user'),
    path('contactadmin/', contactAdminView, name='contact_admin')
]
