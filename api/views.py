from django.shortcuts import render
from rest_framework import viewsets
from .models import Unidade, Curso, Turma, Aluno, TipoResiduos, Reciclagem
from .serializers import *

# Create your views here.
class UnidadeViewSet(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class TipoResiduosViewSet(viewsets.ModelViewSet):
    queryset = TipoResiduos.objects.all()
    serializer_class = TipoResiduosSerializer

class ReciclagemViewSet(viewsets.ModelViewSet):
    queryset = Reciclagem.objects.all()
    serializer_class = ReciclagemSerializer
