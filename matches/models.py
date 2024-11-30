from django.db import models

# Create your models here.
from django.db import models
from players.models import Player
from players.models import Player

class Match(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="matches")
    opponent = models.CharField(max_length=100)
    date = models.DateField()
    result = models.CharField(max_length=10)  # e.g., "Win" or "Loss"
    score = models.CharField(max_length=50)  # e.g., "6-4, 6-3"

    def __str__(self):
        return f"{self.player.name} vs {self.opponent} on {self.date}"
