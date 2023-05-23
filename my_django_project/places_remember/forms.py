from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
import datetime


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class MemoryForm(forms.Form):
    title = forms.CharField(max_length=100)
    comment = forms.CharField(widget=forms.Textarea)
    date = forms.DateField(initial=datetime.date.today)
