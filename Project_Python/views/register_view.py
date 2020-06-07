from django.views import View
from django.views.generic import CreateView


class CreatePositionView(CreateView):
    model = Position
    fields = ['name', 'min_salary', 'max_salary']
    success_message = "Entry was created successfully"
    success_url = reverse_lazy('all_positions')
    login_url = reverse_lazy('index')