from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    ranking = models.IntegerField()
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.name
