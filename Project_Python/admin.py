from django.contrib import admin

# Register your models here.
from django.contrib import admin

# from Project_Python.models import *
from Project_Python.models import Position, Worker, Tournament

admin.register(Position)
admin.register(Worker)
admin.register(Tournament)
