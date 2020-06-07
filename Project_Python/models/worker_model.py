from django.db import models

# from Project_Python.models import Position
# from my_project.Project_Python.models import Position
from Project_Python.models import Position


class Worker(models.Model):
    id = models.AutoField(db_index=True, primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)