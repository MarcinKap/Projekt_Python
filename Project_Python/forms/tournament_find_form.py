from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Projekt import settings


class TournamentFindForm(forms.Form):
    class Meta:
        start_date = forms.DateField()
        end_date = forms.DateField()
