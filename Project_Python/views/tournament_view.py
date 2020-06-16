from django.views.generic import ListView
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
from Project_Python.models import Tournament, PlayerTournament


class AllTournamentView(ListView):
    model = Tournament
    login_url = reverse_lazy('index')
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        logger.debug('AllTournamentView.get_context_data')

        tournaments = Tournament.objects.all( )
        for x in range(0, tournaments.count()):
            id_tournament = Tournament.objects.all()[x].id
            new_current_participiants = PlayerTournament.objects.filter(tournament = x).count()
            Tournament.objects.filter(id=id_tournament-1).update(current_number_participants= new_current_participiants)

        context = super().get_context_data(**kwargs)

        context['now'] = timezone.now()
        return context


class DetailTournamentView(LoginRequiredMixin, DetailView):
    model = Tournament
    login_url = reverse_lazy('index')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CreateTournamentView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Tournament
    fields = ['id', 'name', 'max_number_participants', 'start_date']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_tournament')
    login_url = reverse_lazy('index')

class UpdateViewForTournament(SingleObjectTemplateResponseMixin, BaseUpdateView):
    template_name_suffix = '_update'


class UpdateTournamentView(LoginRequiredMixin, SuccessMessageMixin, UpdateViewForTournament):
    model = Tournament

    fields = ['id', 'name', 'max_number_participants', 'start_date']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_tournament')
    login_url = reverse_lazy('index')


class DeleteTournamentView(LoginRequiredMixin, DeleteView):
    model = Tournament
    login_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('all_tournament')
