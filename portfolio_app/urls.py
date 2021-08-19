from django.urls import path
from .views import my_portfolio

app_name = 'portfolio'
urlpatterns = [
    path('<str:username>/', my_portfolio, name='portfolio'),
]

