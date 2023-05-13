from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    pass


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ( 'email', 'role')
