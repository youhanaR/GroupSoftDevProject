# Author: Jem Challis

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 



urlpatterns = [
    #Sort the recycling Paths
    path('str_intro/', views.str_intro, name='str_intro'),
    path('str_game/', views.str_game, name='str_game'),
    path('str_end/', views.str_end, name='str_end'),
]