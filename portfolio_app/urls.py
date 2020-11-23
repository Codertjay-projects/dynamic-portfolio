from django.urls import path
from .views import  my_portfolio,HomeView

app_name = 'portfolio'
urlpatterns = [
    path('<str:username>/', my_portfolio,name='portfolio'),
    path('', HomeView,name='home'),
]
