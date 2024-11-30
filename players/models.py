from django.db import models

class AtpPlayers(models.Model):
    player_id = models.IntegerField(primary_key=True)
    name_first = models.CharField(max_length=100, blank=True, null=True)
    name_last = models.CharField(max_length=100, blank=True, null=True)
    hand = models.CharField(max_length=5, blank=True, null=True)
    dob = models.IntegerField(blank=True, null=True)
    ioc = models.CharField(max_length=3, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    wikidata_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'atp_players'
        managed = False


    def __str__(self):
        return f"{self.name_first} {self.name_last}"
