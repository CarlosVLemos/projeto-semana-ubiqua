from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Unidade, TipoResiduos, Curso, Turma, Aluno, Reciclagem
from .forms import UnidadeForm, TipoResiduosForm, CursoForm, TurmaForm, AlunoForm, ReciclagemForm
from .serializers import CidadeSerializer, EstadoSerializer, UnidadeSerializer, CursoSerializer, TurmaSerializer, AlunoSerializer, TipoResiduosSerializer, ReciclagemSerializer
from rest_framework import viewsets




# ---------- UNIDADES ----------
class UnidadeListView(ListView):
    model = Unidade
    template_name = 'reciclagem/unidade_list.html'
    context_object_name = 'unidades'

class UnidadeCreateView(CreateView):
    model = Unidade
    form_class = UnidadeForm
    template_name = 'reciclagem/unidade_form.html'
    success_url = reverse_lazy('reciclagem:unidade_list')

class UnidadeUpdateView(UpdateView):
    model = Unidade
    form_class = UnidadeForm
    template_name = 'reciclagem/unidade_form.html'
    success_url = reverse_lazy('reciclagem:unidade_list')

class UnidadeDeleteView(DeleteView):
    model = Unidade
    template_name = 'reciclagem/unidade_confirm_delete.html'
    success_url = reverse_lazy('reciclagem:unidade_list')

def unidade_delete(request, pk):
    get_object_or_404(Unidade, pk=pk).delete()
    return redirect('reciclagem:unidade_list')


# ---------- TIPOS DE RESÍDUO ----------
# class TipoResiduoListView(ListView):
#     model               = TipoResiduo
#     template_name       = 'reciclagem/tiporesiduo_list.html'
#     context_object_name = 'tipos'

# class TipoResiduoCreateView(CreateView):
#     model         = TipoResiduo
#     form_class    = TipoResiduoForm
#     template_name = 'reciclagem/tiporesiduo_form.html'
#     success_url   = reverse_lazy('reciclagem:tiporesiduo_list')

# class TipoResiduoUpdateView(UpdateView):
#     model         = TipoResiduo
#     form_class    = TipoResiduoForm
#     template_name = 'reciclagem/tiporesiduo_form.html'
#     success_url   = reverse_lazy('reciclagem:tiporesiduo_list')

# class TipoResiduoDeleteView(DeleteView):
#     model         = TipoResiduo
#     template_name = 'reciclagem/tiporesiduo_confirm_delete.html'
#     success_url   = reverse_lazy('reciclagem:tiporesiduo_list')




def tiporesiduos_delete(request, pk):
    get_object_or_404(TipoResiduos, pk=pk).delete()
    return redirect('reciclagem:tiporesiduos_list')

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

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
