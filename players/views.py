from django.db.models import Q  # Import Q for complex queries
from django.shortcuts import render
from players.models import AtpPlayers
from .forms import PlayerQueryForm

def query_player(request):
    form = PlayerQueryForm(request.GET or None)
    players = None

    if form.is_valid():
        name = form.cleaned_data.get("name")
        dob = form.cleaned_data.get("dob")
        hand = form.cleaned_data.get("hand")
        ioc = form.cleaned_data.get("ioc")
        height = form.cleaned_data.get("height")
        wikidata_id = form.cleaned_data.get("wikidata_id")

        # Build the query dynamically
        query = Q()
        if name:
            # Split the name input into parts (e.g., "Carlos Alcaraz" -> ["Carlos", "Alcaraz"])
            name_parts = name.split()
            if len(name_parts) == 1:
                # If only one name part, search in both name_first and name_last
                query &= Q(name_first__icontains=name) | Q(name_last__icontains=name)
            else:
                # If two or more name parts, combine queries for both fields
                first_name_query = Q(name_first__icontains=name_parts[0])
                last_name_query = Q(name_last__icontains=name_parts[1])
                query &= first_name_query & last_name_query

        if dob:
            query &= Q(dob=dob)
        if hand:
            query &= Q(hand__iexact=hand)
        if ioc:
            query &= Q(ioc__iexact=ioc)
        if height:
            query &= Q(height=height)
        if wikidata_id:
            query &= Q(wikidata_id__icontains=wikidata_id)

        players = AtpPlayers.objects.filter(query)

    return render(request, "players/query_player.html", {"form": form, "players": players})
