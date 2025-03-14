from django import forms
from .models import GameScore

class NewGameScore(forms.ModelForm):
    class Meta:
        model = GameScore
        fields = ['score']