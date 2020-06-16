from django.contrib.auth.models import User
from django.db import models

from Project_Python.models.player_model import Player

# model turnieju
class Tournament(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    max_number_participants = models.IntegerField( )
    current_number_participants = models.IntegerField(default=0)
    start_date = models.DateField( )
    # players = models.ManyToManyField(Player)
    # users = models.ManyToManyField(User)
    # position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    # def save(self, *args, **kwargs):
    #     print('save() is called.')
    #     super(Tournament, self).save(*args, **kwargs)