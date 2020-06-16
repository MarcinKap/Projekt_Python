from pickle import GET

import self
from django.db.models import Model
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import BaseUpdateView

from Project_Python import logger
# from Project_Python.forms.specify_tournament_player import SpecifyTournamentPlayer
from Project_Python.models import Tournament, PlayerTournament, Player


class CreatePlayerTournamentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PlayerTournament

    fields = ['tournament', 'player']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_tournament')
    login_url = reverse_lazy('index')

    # ref = (self.request.GET).dict( )
    # data = ref['']
    # obj = Tournament.objects.get(pk=int(1))
    # print(obj.__module__)



#
# class CreatePlayerTournamentView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
#     template_name = 'playertournament_form.html'

    # def get(self, request):
    #
    #     players = Player.objects.all( )
    #     tournaments = Tournament.objects.all()
    #
    #     args = {
    #         'players': players, 'tournaments': tournaments
    #     }
    #     return render(request, self.template_name, args)


    #
    # model = PlayerTournament
    #
    #
    # # ref = (self.request.GET).dict( )
    # # data = ref['']
    #
    # tournament = Tournament.objects.get(pk=int(1))
    # # print(obj.__module__)
    # fields = [tournament.name, 'player']
    # success_message = "Entry was created successfully"
    # success_url = reverse_lazy('all_tournament')
    # login_url = reverse_lazy('index')


# def CreatePlayerTournamentView():
#     print(self.kwargs['pk'])
#     context = {
#         'tournament' : Tournament.objects.get(id=int(1)),
#         'players' : Player.objects
#     }
#     return render(GET, 'playertournament_form.html', context)