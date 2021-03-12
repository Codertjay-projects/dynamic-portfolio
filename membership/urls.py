from django.urls import path
from .views import payment_view

app_name = 'membership'
urlpatterns = [
    path('#/<str:payment_type>/', payment_view, name='payment'),
]
