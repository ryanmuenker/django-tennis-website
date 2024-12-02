from django.db.models import Q
from django.shortcuts import render
from players.models import AtpPlayers
from players.models import AtpMatches2023, AtpMatches2024
from players.forms import PlayerQueryForm

def query_player(request):
    form = PlayerQueryForm(request.GET or None)
    players_with_matches = []

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

        # Fetch recent matches for each player
        for player in players:
            recent_matches_2023 = AtpMatches2023.objects.filter(
                Q(winner_id=player.player_id) | Q(loser_id=player.player_id)
            ).order_by('-tourney_date')[:5]

            recent_matches_2024 = AtpMatches2024.objects.filter(
                Q(winner_id=player.player_id) | Q(loser_id=player.player_id)
            ).order_by('-tourney_date')[:5]

            # Combine matches from both years and sort by date
            recent_matches = sorted(
                list(recent_matches_2023) + list(recent_matches_2024),
                key=lambda match: match.tourney_date,
                reverse=True
            )

            players_with_matches.append({
                'player': player,
                'recent_matches': recent_matches[:5]  # Limit to 5 matches
            })

    # Pass the form, players, and matches to the template
    return render(
        request,
        "players/query_player.html",
        {"form": form, "players_with_matches": players_with_matches}
    )
