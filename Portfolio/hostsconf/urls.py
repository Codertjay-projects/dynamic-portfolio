import debug_toolbar
from django.urls import path, include
from .views import my_portfolio

app_name = 'wildcard'
urlpatterns = [
    path('', my_portfolio, name='wildcard_portfolio'),
    path('__debug__/', include(debug_toolbar.urls)),

]
