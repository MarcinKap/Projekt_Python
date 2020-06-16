from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic import CreateView, FormView

from Project_Python.forms.sign_up_form import SignUpForm
from Project_Python.views.guest_view import GuestOnlyView
from Projekt import settings
from django.contrib import messages


class SignUpView(GuestOnlyView, FormView):
    template_name = 'Project_Python/sign_up.html'
    form_class = SignUpForm

    def form_valid(self, form):
        request = self.request
        user = form.save(commit=False)

        # if settings.DISABLE_USERNAME:
        #     # Set a temporary username
        #     user.username = get_random_string()
        # else:
        user.username = form.cleaned_data['username']

        # if settings.ENABLE_USER_ACTIVATION:
        #     user.is_active = False
        user.is_active = True

        # Create a user record
        user.save( )

        # Change the username to the "user_ID" form
        raw_password = form.cleaned_data['password1']

        user = authenticate(username=user.username, password=raw_password)
        login(request, user)

        messages.success(request, 'You are successfully signed up!')

        return redirect('index')
