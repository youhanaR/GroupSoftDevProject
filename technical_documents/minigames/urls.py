# Author: Jem Challis, Rami Youhana

from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 



urlpatterns = [

    #Sort the Recycling Paths
    path('str_intro/', views.str_intro, name='str_intro'),
    path('str_game/', views.str_game, name='str_game'),
    path('str_end/', views.str_end, name='str_end'),

    #Recycle Rush paths
    path('recycle_rush_intro/', views.recycle_rush_intro, name='recycle_rush_intro'), 
    path('recycle_rush/', views.recycle_rush_game, name='recycle_rush_game'),
    path('recycle_rush_end/', views.recycle_rush_end, name='recycle_rush_end'), 
]