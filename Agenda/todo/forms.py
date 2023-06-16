from django.forms import ModelForm
from .models import Todo
from django import forms

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets = {
            'estimated_end': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Titulo',
            'description': 'Descripcion',
            'estimated_end': 'Fecha estimada',
            'priority': 'Prioridad'
        }