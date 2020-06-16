from django.shortcuts import render, redirect
from django.views.generic import CreateView

from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from Project_Python.models import Tournament, PlayerTournament, Player


# class CreatePlayerTournamentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
#     model = PlayerTournament
#
#     # ref = (self.request.GET).dict( )
#     # data = ref['']
#
#     obj = Tournament.objects.get(pk=int(1))
#     # print(obj.__module__)
#
#     fields = ['tournament', 'player']
#     success_message = "Entry was created successfully"
#     success_url = reverse_lazy('all_tournament')
#     login_url = reverse_lazy('index')


class CreatePlayerTournamentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PlayerTournament
    fields = ['tournament', 'player']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_tournament')
    login_url = reverse_lazy('index')


def add_player(request):
    tournament_id = request.POST.get('tournament')
    player_id = request.POST.get('player')
    current_participiants = PlayerTournament.objects.filter(tournament=tournament_id).count( )
    max_participiants = Tournament.objects.get(pk=tournament_id).max_number_participants

    # Sprawdzenie czy dane obiekty juz są w tabeli
    player_tournament_presence = PlayerTournament.objects.filter(tournament=10, player=player_id).count( )

    # Obiekty do zapisania w tabeli
    tournament_object = Tournament.objects.get(pk=tournament_id)
    player_object = Player.objects.get(pk=player_id)

    # Dopisywanie użytkownika do turnieju jeśli liczba max ilosci uczestnikow nie jest przekroczona +
    # sprawdzanie czy gracz jest juz w tablicy
    if max_participiants > current_participiants and player_tournament_presence == 0:
        object = PlayerTournament.objects.create(tournament=tournament_object, player=player_object)

    return redirect('/')

# def CreatePlayerTournamentView(request):
#
#
#     context = {
#         'tournament' : Tournament.objects.get(pk=int(1)),
#         'players' : Player.objects.filter()
#     }
#     return render(request, 'playertournament_form.html', context)
