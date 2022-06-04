from django.urls import re_path as url 
from . import views

# Create URL patterns here
urlpatterns = [ 
    url('^$', views.welcome, name = 'welcome'),
]