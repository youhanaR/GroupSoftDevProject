# Author: Jem Challis, Rami Youhana, Ameera Abdullah

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

    # Whack A Waste Paths
    path('whack_a_waste_intro/', views.whack_a_waste_intro, name='whack_a_waste_intro'),
    path('whack_a_waste/', views.whack_a_waste_game, name='whack_a_waste_game'),
    path('whack_a_waste_end/', views.whack_a_waste_end, name='whack_a_waste_end'),

    # Sea Sweepers Paths
    path('sea_sweepers_intro/', views.sea_sweepers_intro, name='sea_sweepers_intro'),
    path('sea_sweepers/', views.sea_sweepers_game, name='sea_sweepers_game'),
    path('sea_sweepers_end/', views.sea_sweepers_end, name='sea_sweepers_end'),
    
    # Sort N Serve Paths
    path("sns_start/", views.sns_start, name="sns_start"),
    path("sns_game/", views.sns_game, name="sns_game"),
    path("sns_end/", views.sns_end, name="sns_end"),



    # URL pattern to handle saving the game score.
    # When a POST request is made to '/save_score/', the 'save_score' view is triggered.
    # This view processes the score, updates or creates a record in the GameScore model, 
    # and returns a success or error message.
    path('save_score/', views.save_score, name='save_score'),


]