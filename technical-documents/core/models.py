# Author: Ameera Abdullah, Juri Khushayl, Jem Challis
from django.db import models
from django.contrib.auth.models import User
from minigames.models import Game

# Create a location table in the database ~ Ameera, Jem
class Location(models.Model):
    name = models.CharField(max_length=100)
    x_coordinate = models.FloatField()  # Position on the map
    y_coordinate = models.FloatField()
    access_code = models.CharField(max_length=20)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, null=True)  #these are only supposed to be null until games have been added to all relevent locations

    def __str__(self):
        return self.name

# Create a user progress table in the database ~ Ameera
class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.location.name} - {self.location.game.name} - {'Completed' if self.completed else 'Incomplete'}"
    

# Create a profile table in the database ~ Juri
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username