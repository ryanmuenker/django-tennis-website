# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AtpMatches2023(models.Model):
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
    w_1stin = models.IntegerField(db_column='w_1stIn', blank=True, null=True)  # Field name made lowercase.
    w_1stwon = models.IntegerField(db_column='w_1stWon', blank=True, null=True)  # Field name made lowercase.
    w_2ndwon = models.IntegerField(db_column='w_2ndWon', blank=True, null=True)  # Field name made lowercase.
    w_svgms = models.IntegerField(db_column='w_SvGms', blank=True, null=True)  # Field name made lowercase.
    w_bpsaved = models.IntegerField(db_column='w_bpSaved', blank=True, null=True)  # Field name made lowercase.
    w_bpfaced = models.IntegerField(db_column='w_bpFaced', blank=True, null=True)  # Field name made lowercase.
    l_ace = models.IntegerField(blank=True, null=True)
    l_df = models.IntegerField(blank=True, null=True)
    l_svpt = models.IntegerField(blank=True, null=True)
    l_1stin = models.IntegerField(db_column='l_1stIn', blank=True, null=True)  # Field name made lowercase.
    l_1stwon = models.IntegerField(db_column='l_1stWon', blank=True, null=True)  # Field name made lowercase.
    l_2ndwon = models.IntegerField(db_column='l_2ndWon', blank=True, null=True)  # Field name made lowercase.
    l_svgms = models.IntegerField(db_column='l_SvGms', blank=True, null=True)  # Field name made lowercase.
    l_bpsaved = models.IntegerField(db_column='l_bpSaved', blank=True, null=True)  # Field name made lowercase.
    l_bpfaced = models.IntegerField(db_column='l_bpFaced', blank=True, null=True)  # Field name made lowercase.
    winner_rank = models.IntegerField(blank=True, null=True)
    winner_rank_points = models.IntegerField(blank=True, null=True)
    loser_rank = models.IntegerField(blank=True, null=True)
    loser_rank_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_matches_2023'


class AtpMatches2024(models.Model):
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
    w_1stin = models.IntegerField(db_column='w_1stIn', blank=True, null=True)  # Field name made lowercase.
    w_1stwon = models.IntegerField(db_column='w_1stWon', blank=True, null=True)  # Field name made lowercase.
    w_2ndwon = models.IntegerField(db_column='w_2ndWon', blank=True, null=True)  # Field name made lowercase.
    w_svgms = models.IntegerField(db_column='w_SvGms', blank=True, null=True)  # Field name made lowercase.
    w_bpsaved = models.IntegerField(db_column='w_bpSaved', blank=True, null=True)  # Field name made lowercase.
    w_bpfaced = models.IntegerField(db_column='w_bpFaced', blank=True, null=True)  # Field name made lowercase.
    l_ace = models.IntegerField(blank=True, null=True)
    l_df = models.IntegerField(blank=True, null=True)
    l_svpt = models.IntegerField(blank=True, null=True)
    l_1stin = models.IntegerField(db_column='l_1stIn', blank=True, null=True)  # Field name made lowercase.
    l_1stwon = models.IntegerField(db_column='l_1stWon', blank=True, null=True)  # Field name made lowercase.
    l_2ndwon = models.IntegerField(db_column='l_2ndWon', blank=True, null=True)  # Field name made lowercase.
    l_svgms = models.IntegerField(db_column='l_SvGms', blank=True, null=True)  # Field name made lowercase.
    l_bpsaved = models.IntegerField(db_column='l_bpSaved', blank=True, null=True)  # Field name made lowercase.
    l_bpfaced = models.IntegerField(db_column='l_bpFaced', blank=True, null=True)  # Field name made lowercase.
    winner_rank = models.IntegerField(blank=True, null=True)
    winner_rank_points = models.IntegerField(blank=True, null=True)
    loser_rank = models.IntegerField(blank=True, null=True)
    loser_rank_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_matches_2024'


class AtpMatchesQualChall2023(models.Model):
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
    loser_ht = models.TextField(blank=True, null=True)
    loser_ioc = models.TextField(blank=True, null=True)
    loser_age = models.FloatField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    best_of = models.IntegerField(blank=True, null=True)
    round = models.TextField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    w_ace = models.IntegerField(blank=True, null=True)
    w_df = models.IntegerField(blank=True, null=True)
    w_svpt = models.IntegerField(blank=True, null=True)
    w_1stin = models.IntegerField(db_column='w_1stIn', blank=True, null=True)  # Field name made lowercase.
    w_1stwon = models.IntegerField(db_column='w_1stWon', blank=True, null=True)  # Field name made lowercase.
    w_2ndwon = models.IntegerField(db_column='w_2ndWon', blank=True, null=True)  # Field name made lowercase.
    w_svgms = models.IntegerField(db_column='w_SvGms', blank=True, null=True)  # Field name made lowercase.
    w_bpsaved = models.IntegerField(db_column='w_bpSaved', blank=True, null=True)  # Field name made lowercase.
    w_bpfaced = models.IntegerField(db_column='w_bpFaced', blank=True, null=True)  # Field name made lowercase.
    l_ace = models.IntegerField(blank=True, null=True)
    l_df = models.IntegerField(blank=True, null=True)
    l_svpt = models.IntegerField(blank=True, null=True)
    l_1stin = models.IntegerField(db_column='l_1stIn', blank=True, null=True)  # Field name made lowercase.
    l_1stwon = models.IntegerField(db_column='l_1stWon', blank=True, null=True)  # Field name made lowercase.
    l_2ndwon = models.IntegerField(db_column='l_2ndWon', blank=True, null=True)  # Field name made lowercase.
    l_svgms = models.IntegerField(db_column='l_SvGms', blank=True, null=True)  # Field name made lowercase.
    l_bpsaved = models.IntegerField(db_column='l_bpSaved', blank=True, null=True)  # Field name made lowercase.
    l_bpfaced = models.IntegerField(db_column='l_bpFaced', blank=True, null=True)  # Field name made lowercase.
    winner_rank = models.IntegerField(blank=True, null=True)
    winner_rank_points = models.IntegerField(blank=True, null=True)
    loser_rank = models.TextField(blank=True, null=True)
    loser_rank_points = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_matches_qual_chall_2023'


class AtpMatchesQualChall2024(models.Model):
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
    winner_ht = models.TextField(blank=True, null=True)
    winner_ioc = models.TextField(blank=True, null=True)
    winner_age = models.FloatField(blank=True, null=True)
    loser_id = models.IntegerField(blank=True, null=True)
    loser_seed = models.IntegerField(blank=True, null=True)
    loser_entry = models.TextField(blank=True, null=True)
    loser_name = models.TextField(blank=True, null=True)
    loser_hand = models.TextField(blank=True, null=True)
    loser_ht = models.TextField(blank=True, null=True)
    loser_ioc = models.TextField(blank=True, null=True)
    loser_age = models.FloatField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    best_of = models.IntegerField(blank=True, null=True)
    round = models.TextField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    w_ace = models.IntegerField(blank=True, null=True)
    w_df = models.IntegerField(blank=True, null=True)
    w_svpt = models.IntegerField(blank=True, null=True)
    w_1stin = models.IntegerField(db_column='w_1stIn', blank=True, null=True)  # Field name made lowercase.
    w_1stwon = models.IntegerField(db_column='w_1stWon', blank=True, null=True)  # Field name made lowercase.
    w_2ndwon = models.IntegerField(db_column='w_2ndWon', blank=True, null=True)  # Field name made lowercase.
    w_svgms = models.IntegerField(db_column='w_SvGms', blank=True, null=True)  # Field name made lowercase.
    w_bpsaved = models.IntegerField(db_column='w_bpSaved', blank=True, null=True)  # Field name made lowercase.
    w_bpfaced = models.IntegerField(db_column='w_bpFaced', blank=True, null=True)  # Field name made lowercase.
    l_ace = models.IntegerField(blank=True, null=True)
    l_df = models.IntegerField(blank=True, null=True)
    l_svpt = models.IntegerField(blank=True, null=True)
    l_1stin = models.IntegerField(db_column='l_1stIn', blank=True, null=True)  # Field name made lowercase.
    l_1stwon = models.IntegerField(db_column='l_1stWon', blank=True, null=True)  # Field name made lowercase.
    l_2ndwon = models.IntegerField(db_column='l_2ndWon', blank=True, null=True)  # Field name made lowercase.
    l_svgms = models.IntegerField(db_column='l_SvGms', blank=True, null=True)  # Field name made lowercase.
    l_bpsaved = models.IntegerField(db_column='l_bpSaved', blank=True, null=True)  # Field name made lowercase.
    l_bpfaced = models.IntegerField(db_column='l_bpFaced', blank=True, null=True)  # Field name made lowercase.
    winner_rank = models.IntegerField(blank=True, null=True)
    winner_rank_points = models.IntegerField(blank=True, null=True)
    loser_rank = models.IntegerField(blank=True, null=True)
    loser_rank_points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_matches_qual_chall_2024'


class AtpPlayers(models.Model):
    player_id = models.IntegerField(blank=True, null=True)
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


class AtpRankingsCurrent(models.Model):
    ranking_date = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    player = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atp_rankings_current'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class MatchesMatch(models.Model):
    id = models.BigAutoField(primary_key=True)
    opponent = models.CharField(max_length=100)
    date = models.DateField()
    result = models.CharField(max_length=10)
    score = models.CharField(max_length=50)
    player = models.ForeignKey('PlayersPlayer', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'matches_match'


class PlayersPlayer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    ranking = models.IntegerField()
    nationality = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'players_player'
