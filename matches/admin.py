from django.contrib import admin
from .models import Match

class MatchAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('player', 'opponent', 'date', 'result', 'score')
    
    # Fields to use as filters in the admin interface
    list_filter = ('result', 'date')
    
    # Fields to search in the admin interface
    search_fields = ('player__name_first', 'player__name_last', 'opponent')
    
    # Fields to use as ordering in the admin list view
    ordering = ('-date',)

# Register the Match model with the admin interface
admin.site.register(Match, MatchAdmin)
