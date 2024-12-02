from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query_player, name='query_player'),
    path('player/<int:player_id>/', views.player_matches, name='player_matches'),  # New URL pattern
]
