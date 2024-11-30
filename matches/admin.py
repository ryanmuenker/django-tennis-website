# Register your models here.
from django.contrib import admin
from .models import AtpPlayers

class AtpPlayersAdmin(admin.ModelAdmin):
    list_display = ('name_first', 'name_last', 'ioc', 'height', 'dob')  # Fields to display

admin.site.register(AtpPlayers, AtpPlayersAdmin)

