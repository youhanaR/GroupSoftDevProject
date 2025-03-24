# Author: Jem Challis

from django.db import models
from django.contrib.auth.models import User
from django.apps import apps


#Jem
class GameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    minigame = models.ForeignKey(
        'core.Minigame',  # Reference the model using the app label
        on_delete=models.CASCADE
    )
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.minigame.name} - {self.score}"
