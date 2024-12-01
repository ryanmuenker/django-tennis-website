from django.db import models

class AtpPlayers(models.Model):
    player_id = models.IntegerField(primary_key = True)
    name_first = models.TextField(blank=True, null=True)
    name_last = models.TextField(blank=True, null=True)
    hand = models.TextField(blank=True, null=True)
    dob = models.IntegerField(blank=True, null=True)
    ioc = models.TextField(blank=True, null=True)
    height = models.TextField(blank=True, null=True)
    wikidata_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_players'

    def __str__(self):
        return f"{self.name_first} {self.name_last}"
