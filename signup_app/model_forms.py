from django.forms import ModelForm
from signup_app.models import User

__author__ = 'shannon'

class UserForm(ModelForm):
    class Meta:
        model=User
        fields = ['email',]