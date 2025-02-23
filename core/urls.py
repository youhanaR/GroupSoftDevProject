
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views 


urlpatterns = [
    
    path("", views.landing_page, name="landing"), #Default page
    
    path("register", views.register, name="register"),
   
    path('my-login', views.my_login, name="my-login"),
    
    path('dashboard', views.dashboard, name="dashboard"),
   
    path('user-logout', views.user_logout, name='user-logout'),
    
    path('user-profile', views.user_profile, name="user-profile"), # you can acess the user profile by username
    path('delete-account', views.deleteAccount, name="delete-account"),
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
   
 