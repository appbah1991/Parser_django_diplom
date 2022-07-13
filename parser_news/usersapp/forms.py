from django.contrib.auth.forms import UserCreationForm
from .models import Parser_User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Parser_User
        fields = ('username', 'password1', 'password2', 'email')
