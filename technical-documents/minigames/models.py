# Author: Jem Challis

from django.db import models
from django.contrib.auth.models import User

# Jem
class Game(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()  # URL of the minigame page
    def __str__(self):
        return f"{self.name}"

# Jem
class GameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    score = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user.username} - {self.game.name} - {self.score}"