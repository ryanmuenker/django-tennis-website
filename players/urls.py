from django.urls import path
from . import views

urlpatterns = [
    path('query/', views.query_player, name='query_player'),  # The correct pattern for 'players/query/'
]
