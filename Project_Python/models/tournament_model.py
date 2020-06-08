from django.contrib.auth.models import User
from django.db import models


# from Project_Python.models import Position
# from my_project.Project_Python.models import Position

class Tournament(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    max_number_participants = models.IntegerField( )
    current_number_participants = models.IntegerField( )
    start_date = models.DateField( )
    # users = User.objects.values_list('id', 'username')
    # position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
