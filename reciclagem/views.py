from django.shortcuts import render, redirect, get_object_or_404
from .models import Reciclagem
from .forms  import ReciclagemForm

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