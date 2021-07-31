from django.urls import path

from service.views import UserServiceCreate, services_update_view, service_delete_view

app_name = 'service'
urlpatterns = [

    path('serviceCreate/', UserServiceCreate.as_view(), name='serviceCreate'),
    path('serviceUpdate/', services_update_view, name='serviceUpdate'),
    path('serviceDelete/', service_delete_view, name='serviceDelete'),
]
