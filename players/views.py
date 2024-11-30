from django.db.models import Q  # Import Q for complex queries
from django.shortcuts import render
from .models import AtpPlayer
from .forms import PlayerQueryForm

def query_player(request):
    form = PlayerQueryForm(request.GET or None)
    players = None

    if form.is_valid():
        name = form.cleaned_data.get("name")
        if name:
            # Query both name_first and name_last fields
            players = AtpPlayer.objects.filter(
                Q(name_first__icontains=name) | Q(name_last__icontains=name)
            )
            print(players)  # Debugging output to ensure results are returned

    return render(request, "players/query_player.html", {"form": form, "players": players})
