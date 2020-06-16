from django.db import models

# from Project_Python.models import Position
# from my_project.Project_Python.models import Position
from Project_Python.models import Tournament, Player

# model fazy turnieju
class TournamentPhase(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return str('Tournament name: ' + str(self.name) + '   Player id: ' + str(self.tournament.id))
