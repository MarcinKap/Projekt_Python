"""Projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from Project_Python import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include
from django.contrib import admin
from django.urls import path

from Project_Python.views import NewLoginView, NewLogoutView, AllPositionView, CreatePositionView, UpdatePositionView, \
    DetailPositionView, DeletePositionView, WorkerListView, CreateWorkerView, UpdateWorkerView, DeleteWorkerView, \
    AvgWorkersView, IndexView
from Project_Python.views.register_view import SignUpView
# from Project_Python.views.tournament import TournamentCreatorView
from Project_Python.views.tournament import CreateTournamentView, UpdateTournamentView, DetailTournamentView, \
    DeleteTournamentView, AllTournamentView

urlpatterns = [
    path('', IndexView.as_view( ), name='index'),
    path('logout', NewLogoutView.as_view( ), name='logout'),
    path('logout', NewLogoutView.as_view( ), name='logout'),
    path('positions', AllPositionView.as_view( ), name="all_positions"),
    path('positions/add/', CreatePositionView.as_view( ), name="position_add"),
    path('positions/<int:pk>/update', UpdatePositionView.as_view( ), name="position_update"),
    path('positions/<int:pk>/', DetailPositionView.as_view( ), name="position_detail"),
    path('positions/<int:pk>/delete', DeletePositionView.as_view( ), name="position_delete"),
    path('workers', WorkerListView.as_view( ), name='all_workers'),
    path('workers/add/', CreateWorkerView.as_view( ), name="worker_add"),
    path('workers/<int:pk>/update', UpdateWorkerView.as_view( ), name="worker_update"),
    path('workers/<int:pk>/delete', DeleteWorkerView.as_view( ), name="worker_delete"),
    path('avg_workers', AvgWorkersView.as_view( ), name='avg_workers'),

    path('admin/', admin.site.urls),
    # path('Project_Python/', include('Project_Python.urls')),

    # NOWE
    path('sign_up', SignUpView.as_view( ), name='sign_up'),
    # path('tournament_creator', TournamentCreatorView.as_view( ), name='tournament_creator'),
    path('tournaments', AllTournamentView.as_view( ), name="all_tournament"),
    path('tournaments/add/', CreateTournamentView.as_view( ), name="tournament_add"),
    path('tournaments/<int:pk>/update', UpdateTournamentView.as_view( ), name="tournament_update"),
    path('tournaments/<int:pk>/', DetailTournamentView.as_view( ), name="tournament_detail"),
    path('tournaments/<int:pk>/delete', DeleteTournamentView.as_view( ), name="tournament_delete"),

    path('log_in', NewLoginView.as_view( ), name="tournament_delete"),




]
