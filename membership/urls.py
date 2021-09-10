from django.urls import path
from .views import payment_view,payment_done

app_name = 'membership'
urlpatterns = [
    path('#/<str:payment_type>/', payment_view, name='payment_progress'),
    path('#/#/payment_done/', payment_done, name='payment_done'),
]
