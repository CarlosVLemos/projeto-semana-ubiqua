
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from .models import *
from .forms import UnidadeForm

'''
def ser_recicla(request, pk=None):
    """
    Se pk for passado, faz edição; senão cria novo.
    Sempre exibe form + tabela de registros.
    """
    if pk:
        instancia = get_object_or_404(Reciclagem, pk=pk)
    else:
        instancia = None

    if request.method == 'POST':
        form = ReciclagemForm(request.POST, instance=instancia)
        if form.is_valid():
            form.save()
            return redirect('reciclagem:ser_recicla_list')
    else:
        form = ReciclagemForm(instance=instancia)

    registros = Reciclagem.objects.all().order_by('-criado_em')
    return render(request, 'reciclagem/ser_recicla.html', {
        'form': form,
        'registros': registros,
        'edit': True if pk else False,
    })

def ser_recicla_delete(request, pk):
    """
    Exclui sem confirmação extra.
    """
    get_object_or_404(Reciclagem, pk=pk).delete()
    return redirect('reciclagem:ser_recicla_list')

'''

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

'''
# ---------- TIPOS DE RESÍDUO ----------
class TipoResiduoListView(ListView):
    model               = TipoResiduo
    template_name       = 'reciclagem/tiporesiduo_list.html'
    context_object_name = 'tipos'

class TipoResiduoCreateView(CreateView):
    model         = TipoResiduo
    form_class    = TipoResiduoForm
    template_name = 'reciclagem/tiporesiduo_form.html'
    success_url   = reverse_lazy('reciclagem:tiporesiduo_list')

class TipoResiduoUpdateView(UpdateView):
    model         = TipoResiduo
    form_class    = TipoResiduoForm
    template_name = 'reciclagem/tiporesiduo_form.html'
    success_url   = reverse_lazy('reciclagem:tiporesiduo_list')

class TipoResiduoDeleteView(DeleteView):
    model         = TipoResiduo
    template_name = 'reciclagem/tiporesiduo_confirm_delete.html'
    success_url   = reverse_lazy('reciclagem:tiporesiduo_list')

'''