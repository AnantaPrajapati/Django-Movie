from django import forms
from .models import Movie, Profile
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_icon', 'movie_title', 'release_date', 'actor', 'director','description', 'country']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ['gender', 'city']
