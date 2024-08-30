from django import forms
from .models import CityDescription

class CityDescriptionForm(forms.ModelForm):
    class Meta:
        model = CityDescription
        fields = ['city_description', 'best_food', 'best_place_to_visit', 'rating']
        widgets = {
            'city_description': forms.Textarea(attrs={'placeholder':'Describe the city'}),
            'best_food': forms.TextInput(attrs={'placeholder':'Enter the best food.'}),
            'best_place_to_visit': forms.TextInput(attrs={'placeholder': 'Enter the best place to visit.'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5, 'placeholder': 'Rate out of 5.'})
        }
        labels = {
            'best_food': 'Best food to eat',
            'best_place_to_visit': 'Best place to visit.',
            'rating': 'Rate experience',
        }