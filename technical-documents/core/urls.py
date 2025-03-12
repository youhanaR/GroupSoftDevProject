# Author: Surin Chai, Ameera Abdullah, Juri Kushayi

"""
urls.py

This module defines the URL patterns for the Django application. For the prototype, it includes 
routes for user authentication, dashboard access, password reset functionality, and game 
descriptions based on location.

Author: Juri Khushayl, Surin Wi Sut, Ameera Abdullah
"""


from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 


urlpatterns = [
    #Default Page
    path("", views.landing_page, name="landing"), 
    

    path("register/", views.register, name="register"),
    path('my-login/', views.my_login, name="my-login"),
    path('dashboard/', views.dashboard, name="dashboard"),
   
    #User-Related Paths
    path('user-logout/', views.user_logout, name='user-logout'),
    path('user-profile', views.user_profile, name="user-profile"), 
    path('delete-account', views.deleteAccount, name="delete-account"),
    
    #Password Reset Related Paths
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    #Registration Email Confirmation Related Paths
    path('checkyouremail', views.check_your_email, name='check-your-email'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('activation-success/', views.activation_success, name='activation-success'),

    #Privacy Policy Page
    path('privacy-policy/', views.privacy_policy, name='privacy-policy'),

    #Dynamic paths for the game description page
    path('game/description/<str:location>/', views.game_description, name='game_description'),

    #Overall Leaderboard Page
    path('leaderboard/', views.leaderboard, name='leaderboard'),

]
   
 