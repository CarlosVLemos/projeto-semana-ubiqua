from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

def generate_views(modelo, form=None, paginacao=10, template_dir=''):
    """
    Gera as views baseadas no modelo e nos parâmetros fornecidos.
    
    :param modelo: Modelo do Django.
    :param form: Classe de formulário associada.
    :param paginacao: Número de itens por página na ListView.
    :param template_dir: Diretório onde os templates estão armazenados.
    :return: Dicionário contendo as views geradas.
    """

    class GeneratedListView(UserPassesTestMixin, ListView):
        model = modelo
        template_name = f'{template_dir}/{modelo._meta.model_name}_list.html'
        paginate_by = paginacao
        context_object_name = 'items'

        def test_func(self):
            return self.request.user.has_perm(f'{modelo._meta.app_label}.view_{modelo._meta.model_name}')

    class GeneratedCreateView(UserPassesTestMixin, CreateView):
        model = modelo
        form_class = form
        template_name = f'{template_dir}/{modelo._meta.model_name}_form.html'
        success_url = f'/{modelo._meta.model_name}'

        def test_func(self):
            return self.request.user.has_perm(f'{modelo._meta.app_label}.add_{modelo._meta.model_name}')

    class GeneratedUpdateView(UserPassesTestMixin, UpdateView):
        model = modelo
        form_class = form
        template_name = f'{template_dir}/{modelo._meta.model_name}_form.html'
        success_url = f'/{modelo._meta.model_name}'

        def test_func(self):
            return self.request.user.has_perm(f'{modelo._meta.app_label}.change_{modelo._meta.model_name}')

    def generated_delete_object(request, pk):
        get_object_or_404(modelo, pk=pk).delete()
        return redirect(f'reciclagem:{modelo._meta.model_name}_list')

    return {
        'list_view': GeneratedListView,
        'create_view': GeneratedCreateView,
        'update_view': GeneratedUpdateView,
        'delete_view': generated_delete_object,
    }
