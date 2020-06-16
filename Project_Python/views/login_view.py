from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

# Logowanie
class NewLoginView(LoginView):
    template_name = 'Project_Python/log_in.html'

    def get_success_url(self):
        messages.success(self.request, 'A user successfully logged in')
        return reverse_lazy('all_tournament')

#Wylogowywanie
class NewLogoutView(LogoutView):
    def get_next_page(self):
        messages.success(self.request, 'A user successfully logged out')
        return reverse_lazy('index')

