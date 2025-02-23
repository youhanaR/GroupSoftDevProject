from django.contrib import admin
from .models import Profile
# Register your models here.


#Access to Profile in our Admin panel
admin.site.register(Profile)