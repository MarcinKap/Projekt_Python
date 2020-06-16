from django.http import HttpResponse
from django.shortcuts import redirect

from Project_Python.models import Tournament, PlayerTournament, Player
from django.template import loader

from Project_Python.models.tournament_phase_model import TournamentPhase
from Project_Python.models.tournament_phase_player_model import TournamentPhasePlayer

# Strona turnieju z lista faz i graczy
def tournament_phase_list(request, pk):
    phases = TournamentPhase.objects.filter(tournament=pk)
    phases_players = TournamentPhasePlayer.objects.all( )
    players = PlayerTournament.objects.all( ).filter(tournament=pk)
    tournament_id = pk
    template = loader.get_template('tournament_phase_list.html')
    context = {
        'phases_list': phases,
        'player_tournament_list': players,
        'tournament': tournament_id,
        'phases_players': phases_players,
    }
    return HttpResponse(template.render(context, request))

# Dodawanie Fazy po nacisnieciu przycisku
def tournament_phase_add(request, pk):
    number = TournamentPhase.objects.filter(tournament=pk).count( ) + 1
    TournamentPhase.objects.create(name='Phase ' + str(number), tournament=Tournament.objects.get(id=pk))
    # Fazy
    phases = TournamentPhase.objects.filter(tournament=pk)
    # Relacje faza-gracz
    phases_players = TournamentPhasePlayer.objects.all( )
    # Gracze wszyscy
    players = PlayerTournament.objects.all( ).filter(tournament=pk)
    # Przeglądany tournament
    tournament_id = pk

    template = loader.get_template('tournament_phase_list.html')
    context = {
        'phases_list': phases,
        'player_tournament_list': players,
        'tournament': tournament_id,
        'phases_players': phases_players,
    }
    return HttpResponse(template.render(context, request))

# Formatka pod zapis relacji faza - gracz ograniczająca wybór graczy
def tournament_phase_add_player_form(request, pk):
    phase = TournamentPhase.objects.get(id=pk)
    print(phase.id)
    tournament = phase.tournament
    player_tournament_list = PlayerTournament.objects.filter(tournament=tournament.id)
    template = loader.get_template('tournament_add_player_to_phase.html')
    context = {
        'phase': phase,
        'player_tournament_list': player_tournament_list
    }
    return HttpResponse(template.render(context, request))

# Dodawanie relacji faza - gracz
def tournament_phase_add_player_adding(request):
    phase_id = request.GET.get('phase_id')
    player_id = request.GET.get('player_id')
    phase = TournamentPhase.objects.get(id=phase_id)
    tournament = phase.tournament
    # Obiekty do zapisania w tabeli
    player_object = Player.objects.get(pk=player_id)
    object = TournamentPhasePlayer.objects.create(tournament_phase= phase, player=player_object)

    return redirect('/tournaments/phase/' + str(tournament.id) )
