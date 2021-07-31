from django.urls import path

from .views import (userDashboard)

app_name = 'dashboard'

urlpatterns = [
    path('', userDashboard, name='dashboard'),
]
