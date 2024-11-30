from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Player

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    recent_matches = player.matches.all().order_by('-date')[:5]  # Last 5 matches
    return render(request, 'players/player_detail.html', {'player': player, 'recent_matches': recent_matches})
