from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Projekt import settings


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

    email = forms.EmailField(label='Email', help_text='Required. Enter an existing email address.')

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            from django.core.exceptions import ValidationError
            raise ValidationError(_('You can not use this email address.'))

        return email
