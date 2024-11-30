from .models import AtpPlayer
from django.shortcuts import render


def query_player(request):
    name = request.GET.get('name', '')
    players = AtpPlayer.objects.filter(name_first__icontains=name)  # Adjust filter logic if needed
    return render(request, 'players/query_player.html', {'players': players})
