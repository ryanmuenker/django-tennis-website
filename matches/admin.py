from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Match

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('player', 'opponent', 'date', 'result', 'score')  # Fields to display
    search_fields = ('player__name', 'opponent')  # Enable search by player name or opponent
    list_filter = ('date', 'result')  # Filters for date and match result
