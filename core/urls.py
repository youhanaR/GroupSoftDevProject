from django.urls import path
from . import views 

urlpatterns = [
    
    path("", views.landing_page, name="landing"), #Default page
    
    path("register", views.register, name="register"),
   
    path('my-login', views.my_login, name="my-login"),
    
    path('dashboard', views.dashboard, name="dashboard"),
   
    path('user-logout', views.user_logout, name='user-logout'),
]
   
 