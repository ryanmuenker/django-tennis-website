from django.db import models

class Match(models.Model):
    player = models.ForeignKey(
        'players.AtpPlayer',  # String reference to avoid circular import
        on_delete=models.CASCADE,
        related_name="matches"
    )
    opponent = models.CharField(max_length=100)
    date = models.DateField()
    result = models.CharField(max_length=10)
    score = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.player.name_first} {self.player.name_last} vs {self.opponent} on {self.date}"

    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matches"
