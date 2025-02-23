from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    x_coordinate = models.FloatField()  # Position on the map
    y_coordinate = models.FloatField()
    access_code = models.CharField(max_length=20)
    game_url = models.URLField()  # URL of the minigame page

    def __str__(self):
        return self.name

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.location.name} - {'Completed' if self.completed else 'Incomplete'}"
