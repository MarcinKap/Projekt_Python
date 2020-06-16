from django.db import models

# from Project_Python.models import Position
# from my_project.Project_Python.models import Position
from Project_Python.models import Tournament, Player
from Project_Python.models.tournament_phase_model import TournamentPhase

# relacja faza turnieju - gracz
class TournamentPhasePlayer(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    tournament_phase = models.ForeignKey(TournamentPhase, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return str('Tournament id: ' + str(self.tournament_phase.id) + '   Player id: ' + str(self.player.id))
