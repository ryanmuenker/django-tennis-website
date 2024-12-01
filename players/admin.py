from django.contrib import admin
from players.models import AtpPlayers

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id','name_first', 'name_last', 'hand', 'dob', 'ioc', 'height','wikidata_id')

admin.site.register(AtpPlayers, PlayerAdmin)
