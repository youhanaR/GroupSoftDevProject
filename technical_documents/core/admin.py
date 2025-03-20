# Author: Ameera Abdullah, Juri Khushayl

from django.contrib import admin
from .models import Minigame, Location, UserProgress, Profile


# Admin has access to these database
admin.site.register(Minigame)
admin.site.register(Location)
admin.site.register(UserProgress)
admin.site.register(Profile)
