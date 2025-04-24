from django import forms
from .models import *

'''
class TurnoForm(forms.ModelForm):
    class Meta:
        model  = Turno
        fields = ['code', 'nome']
        widgets = {
            'code': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
        }
'''

class UnidadeForm(forms.ModelForm):
    class Meta:
        model  = Unidade
        fields = ['nome', 'endereco', 'cidade', 'estado']
        widgets = {
            'nome':     forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'cidade':   forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'estado':   forms.Select(attrs={'class': 'form-select form-select-sm'}),
        }
        labels = {
            'nome':     'Nome da Unidade',
            'endereco': 'Endereço',
            'cidade':   'Cidade',
            'estado':   'Estado',
        }

class TipoResiduosForm(forms.ModelForm):
    class Meta:
        model  = TipoResiduos
        # só pedimos o nome, o código será slugificado automaticamente
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do material'
        }


'''
class ReciclagemForm(forms.ModelForm):
    class Meta:
        model  = Reciclagem
        fields = [
            'nome', 'matricula', 'turma',
            'turno', 'semestre', 'unidade',
            'tipo_residuo', 'quantidade'
        ]
        widgets = {
            'nome':         forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'matricula':    forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'turma':        forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'turno':        forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'semestre':     forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'unidade':      forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'tipo_residuo': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'quantidade':   forms.NumberInput(attrs={'class': 'form-control form-control-sm'}),
        }

'''