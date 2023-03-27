from django.contrib.auth.forms import UserCreationForm
from .models import AbstractniyUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = AbstractniyUser
        fields = ['username', 'email', 'password']