from django.contrib.auth.models import User
from django.db import models

class Tournament(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    max_number_participants = models.IntegerField( )
    current_number_participants = models.IntegerField(default=0)
    start_date = models.DateField( )
    # users = models.ManyToManyField(User)
    # position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
