from django.urls import path

from .views import (UserProfileUpdate,
                    UserLayoutUpdate,
                    UserNameUpdate)

app_name = 'profile'

urlpatterns = [

    path('profileUpdate/', UserProfileUpdate.as_view(), name='profileUpdate'),
    path('userUpdate/', UserNameUpdate.as_view(), name='userUpdate'),
    path('layoutUpdate/', UserLayoutUpdate.as_view(), name='layoutUpdate'),

]
