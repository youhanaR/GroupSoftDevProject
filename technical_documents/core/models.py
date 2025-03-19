# Author: Ameera Abdullah, Juri Khushayl, Jem Challis
from django.db import models
from django.contrib.auth.models import User
from minigames.models import Game
import random
# Create a location table in the database ~ Ameera
class Location(models.Model):
    name = models.CharField(max_length=100)
    x_coordinate = models.FloatField()  # Position on the map
    y_coordinate = models.FloatField()
    access_code = models.CharField(max_length=20)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, null=True)  #these should only be null until games are added for each location

    def __str__(self):
        return self.name

# Create a user progress table in the database ~ Ameera
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.location.name} - {'Completed' if self.completed else 'Incomplete'}"
    

# Selects a random a icon for profile image from the profile_pics 
def random_cat_image():
    cat_images = [
        "images/profile_pics/cat1.png",
        "images/profile_pics/cat2.png",
        "images/profile_pics/cat3.png",
        "images/profile_pics/cat4.png",
        "images/profile_pics/cat5.png",
        "images/profile_pics/cat6.png",
        "images/profile_pics/cat7.png",
        "images/profile_pics/cat8.png",
        "images/profile_pics/cat9.png",
    ]
    return random.choice(cat_images)

# Create a profile table in the database ~ Juri
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="profile_pics/", default=random_cat_image)#Each user has a profile with a profile picture that defaults to a random cat image.

    def __str__(self):
        return self.user.username