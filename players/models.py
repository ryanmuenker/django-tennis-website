from django.db import models

class AtpPlayers(models.Model):
    player_id = models.IntegerField(primary_key=True)
    name_first = models.TextField(blank=True, null=True)
    name_last = models.TextField(blank=True, null=True)
    hand = models.TextField(blank=True, null=True)
    dob = models.IntegerField(blank=True, null=True)
    ioc = models.TextField(blank=True, null=True)
    height = models.TextField(blank=True, null=True)
    wikidata_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_players'

    def __str__(self):
        return f"{self.name_first} {self.name_last}"


class AtpMatches2023(models.Model):
    id = models.AutoField(primary_key=True)
    tourney_id = models.TextField(blank=True, null=True)
    tourney_name = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    draw_size = models.IntegerField(blank=True, null=True)
    tourney_level = models.TextField(blank=True, null=True)
    tourney_date = models.IntegerField(blank=True, null=True)
    match_num = models.IntegerField(blank=True, null=True)
    winner_id = models.IntegerField(blank=True, null=True)
    winner_seed = models.TextField(blank=True, null=True)
    winner_entry = models.TextField(blank=True, null=True)
    winner_name = models.TextField(blank=True, null=True)
    winner_hand = models.TextField(blank=True, null=True)
    winner_ht = models.IntegerField(blank=True, null=True)
    winner_ioc = models.TextField(blank=True, null=True)
    winner_age = models.FloatField(blank=True, null=True)
    loser_id = models.IntegerField(blank=True, null=True)
    loser_seed = models.TextField(blank=True, null=True)
    loser_entry = models.TextField(blank=True, null=True)
    loser_name = models.TextField(blank=True, null=True)
    loser_hand = models.TextField(blank=True, null=True)
    loser_ht = models.IntegerField(blank=True, null=True)
    loser_ioc = models.TextField(blank=True, null=True)
    loser_age = models.FloatField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    best_of = models.IntegerField(blank=True, null=True)
    round = models.TextField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    w_ace = models.IntegerField(blank=True, null=True)
    w_df = models.IntegerField(blank=True, null=True)
    w_svpt = models.IntegerField(blank=True, null=True)
    w_1stin = models.IntegerField(db_column='w_1stIn', blank=True, null=True)
    w_1stwon = models.IntegerField(db_column='w_1stWon', blank=True, null=True)
    w_2ndwon = models.IntegerField(db_column='w_2ndWon', blank=True, null=True)
    w_svgms = models.IntegerField(db_column='w_SvGms', blank=True, null=True)
    w_bpsaved = models.IntegerField(db_column='w_bpSaved', blank=True, null=True)
    w_bpfaced = models.IntegerField(db_column='w_bpFaced', blank=True, null=True)
    l_ace = models.IntegerField(blank=True, null=True)
    l_df = models.IntegerField(blank=True, null=True)
    l_svpt = models.IntegerField(blank=True, null=True)
    l_1stin = models.IntegerField(db_column='l_1stIn', blank=True, null=True)
    l_1stwon = models.IntegerField(db_column='l_1stWon', blank=True, null=True)
    l_2ndwon = models.IntegerField(db_column='l_2ndWon', blank=True, null=True)
    l_svgms = models.IntegerField(db_column='l_SvGms', blank=True, null=True)
    l_bpsaved = models.IntegerField(db_column='l_bpSaved', blank=True, null=True)
    l_bpfaced = models.IntegerField(db_column='l_bpFaced', blank=True, null=True)
    winner_rank = models.IntegerField(blank=True, null=True)
    winner_rank_points = models.IntegerField(blank=True, null=True)
    loser_rank = models.IntegerField(blank=True, null=True)
    loser_rank_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_matches_2023'


class AtpMatches2024(models.Model):
    id = models.AutoField(primary_key=True)
    tourney_id = models.TextField(blank=True, null=True)
    tourney_name = models.TextField(blank=True, null=True)
    surface = models.TextField(blank=True, null=True)
    draw_size = models.IntegerField(blank=True, null=True)
    tourney_level = models.TextField(blank=True, null=True)
    tourney_date = models.IntegerField(blank=True, null=True)
    match_num = models.IntegerField(blank=True, null=True)
    winner_id = models.IntegerField(blank=True, null=True)
    winner_seed = models.TextField(blank=True, null=True)
    winner_entry = models.TextField(blank=True, null=True)
    winner_name = models.TextField(blank=True, null=True)
    winner_hand = models.TextField(blank=True, null=True)
    winner_ht = models.IntegerField(blank=True, null=True)
    winner_ioc = models.TextField(blank=True, null=True)
    winner_age = models.FloatField(blank=True, null=True)
    loser_id = models.IntegerField(blank=True, null=True)
    loser_seed = models.TextField(blank=True, null=True)
    loser_entry = models.TextField(blank=True, null=True)
    loser_name = models.TextField(blank=True, null=True)
    loser_hand = models.TextField(blank=True, null=True)
    loser_ht = models.IntegerField(blank=True, null=True)
    loser_ioc = models.TextField(blank=True, null=True)
    loser_age = models.FloatField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    best_of = models.IntegerField(blank=True, null=True)
    round = models.TextField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    w_ace = models.IntegerField(blank=True, null=True)
    w_df = models.IntegerField(blank=True, null=True)
    w_svpt = models.IntegerField(blank=True, null=True)
    w_1stin = models.IntegerField(db_column='w_1stIn', blank=True, null=True)
    w_1stwon = models.IntegerField(db_column='w_1stWon', blank=True, null=True)
    w_2ndwon = models.IntegerField(db_column='w_2ndWon', blank=True, null=True)
    w_svgms = models.IntegerField(db_column='w_SvGms', blank=True, null=True)
    w_bpsaved = models.IntegerField(db_column='w_bpSaved', blank=True, null=True)
    w_bpfaced = models.IntegerField(db_column='w_bpFaced', blank=True, null=True)
    l_ace = models.IntegerField(blank=True, null=True)
    l_df = models.IntegerField(blank=True, null=True)
    l_svpt = models.IntegerField(blank=True, null=True)
    l_1stin = models.IntegerField(db_column='l_1stIn', blank=True, null=True)
    l_1stwon = models.IntegerField(db_column='l_1stWon', blank=True, null=True)
    l_2ndwon = models.IntegerField(db_column='l_2ndWon', blank=True, null=True)
    l_svgms = models.IntegerField(db_column='l_SvGms', blank=True, null=True)
    l_bpsaved = models.IntegerField(db_column='l_bpSaved', blank=True, null=True)
    l_bpfaced = models.IntegerField(db_column='l_bpFaced', blank=True, null=True)
    winner_rank = models.IntegerField(blank=True, null=True)
    winner_rank_points = models.IntegerField(blank=True, null=True)
    loser_rank = models.IntegerField(blank=True, null=True)
    loser_rank_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_matches_2024'

class AtpRankingsCurrent(models.Model):
    ranking_date = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    player = models.OneToOneField(  # Use OneToOneField to represent a primary key relationship
        AtpPlayers,
        on_delete=models.CASCADE,
        db_column='player',  # Maps to the `player` column in the database
        primary_key=True  # Explicitly set this as the primary key
    )
    points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False  # Ensure no migrations are applied for this table
        db_table = 'atp_rankings_current'