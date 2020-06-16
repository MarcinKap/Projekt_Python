from django.contrib import admin

# Register your models here.
from django.contrib import admin

from Project_Python.models import *
# from Project_Python.models import Tournament, Player

admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(PlayerTournament)

# admin.register(Tournament)
# admin.register(Player)
