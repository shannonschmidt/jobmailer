from django import forms
from django.forms import ModelForm
from signup_app.models import User

__author__ = 'shannon'

class UserForm(ModelForm):
    class Meta:
        model=User
        exclude = ('signup_date',)
        widgets = {
            'topics': forms.widgets.CheckboxSelectMultiple(),
        }