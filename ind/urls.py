from ind.views import *
from django.urls import path
app_name='cup'

urlpatterns=[
    path('virat/',virat,name='virat'),
]