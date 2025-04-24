from django import forms
from .models import Reciclagem

class ReciclagemForm(forms.ModelForm):
     class Meta:
        model = Reciclagem
        fields = [
            'nome', 'matricula', 'turma',
            'turno', 'semestre', 'unidade',
            'tipo_residuo', 'quantidade'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'turma': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'turno': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'semestre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'unidade': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'tipo_residuo': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        }