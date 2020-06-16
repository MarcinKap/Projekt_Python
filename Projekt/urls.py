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

from Project_Python.views import NewLoginView, NewLogoutView, IndexView, player_tournament_view, tournament_view
from Project_Python.views.player_tournament_view import CreatePlayerTournamentView
from Project_Python.views.player_view import AllPlayersView, CreatePlayerView, DetailPlayerView, DeletePlayerView
from Project_Python.views.register_view import SignUpView
# from Project_Python.views.tournament import TournamentCreatorView
from Project_Python.views.tournament_view import CreateTournamentView, UpdateTournamentView, DetailTournamentView, \
    DeleteTournamentView, AllTournamentView, FindTournamentResult

urlpatterns = [
    path('', IndexView.as_view( ), name='index'),
    path('logout', NewLogoutView.as_view( ), name='logout'),
    path('logout', NewLogoutView.as_view( ), name='logout'),
    # path('positions', AllPositionView.as_view( ), name="all_positions"),
    # path('positions/add/', CreatePositionView.as_view( ), name="position_add"),
    # path('positions/<int:pk>/update', UpdatePositionView.as_view( ), name="position_update"),
    # path('positions/<int:pk>/', DetailPositionView.as_view( ), name="position_detail"),
    # path('positions/<int:pk>/delete', DeletePositionView.as_view( ), name="position_delete"),
    # path('workers', WorkerListView.as_view( ), name='all_workers'),
    # path('workers/add/', CreateWorkerView.as_view( ), name="worker_add"),
    # path('workers/<int:pk>/update', UpdateWorkerView.as_view( ), name="worker_update"),
    # path('workers/<int:pk>/delete', DeleteWorkerView.as_view( ), name="worker_delete"),
    # path('avg_workers', AvgWorkersView.as_view( ), name='avg_workers'),

    path('admin/', admin.site.urls),
    # path('Project_Python/', include('Project_Python.urls')),

    # NOWE
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
    # path('playertournaments/addplayer/<int:pk>', CreatePlayerTournamentView.as_view( ), name="playertournament_add"),

    # Kod zapisujacy turniej i gracza
    path('playertournaments/addplayers', player_tournament_view.add_player, name="add_relation_player_tournament"),


    # path('tournaments/searching', FindTournamentView.as_view(), name="tournament_search"),

    #   ścieżka do strony z forms
    path('tournaments/searching', tournament_view.find_tournament_view, name="tournament_search"),

    # niepotrzbne
    path('findtournamentresult', FindTournamentResult.as_view(), name="tournament_search_result"),

    # wyswietlanie turnieji
    path('findtournamentresult/result', tournament_view.find_tournament_result, name="tournament_search_result2"),




]
