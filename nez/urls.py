from nez.views import *
from django.urls import path
app_name='nocup'
urlpatterns=[
    path('kane/',kane,name='kane'),
]