from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from players.models import AtpPlayers
from players.forms import PlayerQueryForm
from .models import AtpPlayers, AtpMatches2023, AtpMatches2024

def query_player(request):
    form = PlayerQueryForm(request.GET or None)
    players = None  # Initialize players as None

    if form.is_valid():
        # Retrieve form inputs
        name = form.cleaned_data.get("name")
        dob = form.cleaned_data.get("dob")
        hand = form.cleaned_data.get("hand")
        ioc = form.cleaned_data.get("ioc")
        height = form.cleaned_data.get("height")
        wikidata_id = form.cleaned_data.get("wikidata_id")

        # Build the dynamic query
        query = Q()
        if name:
            name_parts = name.split()
            if len(name_parts) == 1:
                query &= Q(name_first__icontains=name) | Q(name_last__icontains=name)
            else:
                query &= Q(name_first__icontains=name_parts[0]) & Q(name_last__icontains=name_parts[1])
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

        # Query the AtpPlayers table
        players = AtpPlayers.objects.filter(query)

    # Pass only the form and players to the template
    return render(
        request,
        "players/query_player.html",
        {"form": form, "players": players}
    )

def player_matches(request, player_id):
    player = get_object_or_404(AtpPlayers, player_id=player_id)

    matches_2023 = AtpMatches2023.objects.filter(
        Q(winner_id=player.player_id) | Q(loser_id=player.player_id)
    ).order_by('-tourney_date')

    matches_2024 = AtpMatches2024.objects.filter(
        Q(winner_id=player.player_id) | Q(loser_id=player.player_id)
    ).order_by('-tourney_date')

    context = {
        'player': player,
        'matches_2023': matches_2023,
        'matches_2024': matches_2024,
    }
    return render(request, 'players/player_matches.html', context)

def match_details(request, match_id, year):
    # Determine which year's match table to query
    if year == "2023":
        match = get_object_or_404(AtpMatches2023, id=match_id)
    elif year == "2024":
        match = get_object_or_404(AtpMatches2024, id=match_id)
    else:
        match = None

    return render(request, "players/match_details.html", {"match": match})