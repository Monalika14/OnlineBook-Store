from django import forms
from .models import Rating

class Reviewform(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['subjects','review','rating']
