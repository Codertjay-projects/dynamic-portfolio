from django.urls import path
from .views import my_portfolio

app_name = 'wildcard'
urlpatterns = [
    path('', my_portfolio, name='wildcard_portfolio'),
]
