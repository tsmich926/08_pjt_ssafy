from django import forms
from .models import Movie,Genre

# Create your forms here.
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meat:
        model = Genre
        fields = '__all__'
