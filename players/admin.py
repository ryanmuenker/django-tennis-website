from django.contrib import admin
from .models import AtpPlayers

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'ranking', 'nationality', 'age', 'height')

admin.site.register(AtpPlayers, PlayerAdmin)
