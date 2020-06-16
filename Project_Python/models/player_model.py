from django.db import models


# from Project_Python.models import Position
# from my_project.Project_Python.models import Position


# model gracza
class Player(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)
