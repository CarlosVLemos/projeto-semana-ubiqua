from django import forms
from .models import *

class UnidadeForm(forms.ModelForm):
    class Meta:
        model  = Unidade
        fields = ['nome', 'endereco', 'cidade', 'estado']
        widgets = {
            'nome':     forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade':   forms.Select(attrs={'class': 'form-select'}),
            'estado':   forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nome':     'Nome da Unidade',
            'endereco': 'Endereço',
            'cidade':   'Cidade',
            'estado':   'Estado',
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model  = Curso
        fields = ['nome', 'duracao', 'coordenador', 'unidade']
        widgets = {
            'nome':         forms.TextInput(attrs={'class': 'form-control'}),
            'duracao':      forms.NumberInput(attrs={'class': 'form-control'}),
            'coordenador':  forms.TextInput(attrs={'class': 'form-control'}),
            'unidade':      forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nome':         'Nome do Curso',
            'duracao':      'Duração (Semestres)',
            'coordenador':  'Coordenador',
            'unidade':      'Unidade',
        }

class TurmaForm(forms.ModelForm):
    class Meta:
        model  = Turma
        fields = ['nome', 'semestre', 'turno', 'curso']
        widgets = {
            'nome':     forms.TextInput(attrs={'class': 'form-control'}),
            'semestre': forms.NumberInput(attrs={'class': 'form-control'}),
            'turno':    forms.Select(attrs={'class': 'form-select'}),
            'curso':    forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nome':     'Nome da Turma',
            'semestre': 'Semestre',
            'turno':    'Turno',
            'curso':    'Curso',
        }

class AlunoForm(forms.ModelForm):
    class Meta:
        model  = Aluno
        fields = ['nome', 'email', 'telefone', 'matricula', 'turma']
        widgets = {
            'nome':      forms.TextInput(attrs={'class': 'form-control'}),
            'email':     forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone':  forms.TextInput(attrs={'class': 'form-control'}),
            'matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'turma':     forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nome':      'Nome do Aluno',
            'email':     'Email',
            'telefone':  'Telefone',
            'matricula': 'Matrícula',
            'turma':     'Turma',
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


class ReciclagemForm(forms.ModelForm):
    class Meta:
        model  = Reciclagem
        fields = ['tipo_residuo', 'quantidade', 'aluno']
        widgets = {
            'tipo_residuo': forms.Select(attrs={'class': 'form-select'}),
            'quantidade':    forms.NumberInput(attrs={'class': 'form-control'}),
            'aluno':         forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'tipo_residuo': 'Tipo de Resíduo',
            'quantidade':    'Quantidade (kg)',
            'aluno':         'Aluno',
        }