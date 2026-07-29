from django import forms
from .models import Trainer

class Trainerform(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'