"""Projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from Project_Python import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include
from django.contrib import admin
from django.urls import path

from Project_Python.views import NewLoginView, NewLogoutView, IndexView, player_tournament_view, tournament_view, \
    tournament_phase_view
from Project_Python.views.player_tournament_view import CreatePlayerTournamentView
from Project_Python.views.player_view import AllPlayersView, CreatePlayerView, DetailPlayerView, DeletePlayerView
from Project_Python.views.register_view import SignUpView
# from Project_Python.views.tournament import TournamentCreatorView
from Project_Python.views.tournament_view import CreateTournamentView, UpdateTournamentView, DetailTournamentView, \
    DeleteTournamentView, AllTournamentView

urlpatterns = [
    path('', IndexView.as_view( ), name='index'),
    path('logout', NewLogoutView.as_view( ), name='logout'),
    path('logout', NewLogoutView.as_view( ), name='logout'),
    path('admin/', admin.site.urls),
    path('sign_up', SignUpView.as_view( ), name='sign_up'),
    # path('tournament_creator', TournamentCreatorView.as_view( ), name='tournament_creator'),
    path('tournaments', AllTournamentView.as_view( ), name="all_tournament"),
    path('tournaments/add/', CreateTournamentView.as_view( ), name="tournament_add"),
    path('tournaments/<int:pk>/', DetailTournamentView.as_view( ), name="tournament_detail"),
    path('tournaments/<int:pk>/delete', DeleteTournamentView.as_view( ), name="tournament_delete"),
    path('tournaments/update/<int:pk>', UpdateTournamentView.as_view( ), name="tournament_update"),

    path('log_in', NewLoginView.as_view( ), name="tournament_delete"),

    path('players', AllPlayersView.as_view( ), name="all_players"),
    path('players/add/', CreatePlayerView.as_view( ), name="player_add"),
    path('players/<int:pk>/', DetailPlayerView.as_view( ), name="player_detail"),
    path('players/<int:pk>/delete', DeletePlayerView.as_view( ), name="player_delete"),

    # Miejsce do wyznaczania turnieju i gracza
    path('playertournaments/addplayer', CreatePlayerTournamentView.as_view( ), name="playertournament_add"),
    # Kod zapisujacy turniej i gracza
    path('playertournaments/addplayers', player_tournament_view.add_player, name="add_relation_player_tournament"),
    #   ścieżka do strony z forms
    path('tournaments/searching', tournament_view.find_tournament_view, name="tournament_search"),
    # wyswietlanie turnieji
    path('findtournamentresult/result', tournament_view.find_tournament_result, name="tournament_search_result2"),

    path('tournaments/phase/<int:pk>', tournament_phase_view.tournament_phase_list, name="tournament_results"),
    path('tournaments/phase_added/<int:pk>', tournament_phase_view.tournament_phase_add, name="phase_add"),
    path('tournaments/phase/add_player/<int:pk>', tournament_phase_view.tournament_phase_add_player_form, name="phase_add_player"),
    path('tournaments/phase/add_player/', tournament_phase_view.tournament_phase_add_player_adding, name="tournament_phase_add_player_adding"),

]
