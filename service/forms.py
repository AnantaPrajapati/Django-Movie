from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_icon', 'movie_title', 'release_date', 'actor', 'description', 'country']
