from players.models import AtpPlayers  # Correctly import from the players app
from django.shortcuts import render


def query_player(request):
    # Get the 'name' parameter from the query string
    name = request.GET.get('name', '')

    # Filter players based on the name
    players = AtpPlayers.objects.filter(name_first__icontains=name)

    # Render the template with the filtered players
    return render(request, 'players/query_player.html', {'players': players})
