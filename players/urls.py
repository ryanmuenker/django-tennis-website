from django.urls import path
from . import views
from .views import home 

urlpatterns = [
    path('query/', views.query_player, name='query_player'),
    path('player/<int:player_id>/', views.player_matches, name='player_matches'),  # New URL pattern
    path('match/<int:match_id>/<str:year>/', views.match_details, name='match_details'),
    path('', home, name='home'),  # Home page
]
