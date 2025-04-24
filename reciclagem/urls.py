
from django.urls import path
from .views import *
from .forms import *
from utils.generate_view import generate_views

app_name = 'reciclagem'

tipo_residuos = generate_views(TipoResiduos, TipoResiduosForm, 10, template_dir='tiporesiduos')

urlpatterns = [
    path('unidades/', UnidadeListView.as_view(), name='unidade_list'),
    path('unidades/novo/', UnidadeCreateView.as_view(), name='unidade_create'),
    path('unidades/<int:pk>/editar/', UnidadeUpdateView.as_view(), name='unidade_update'),
    path('unidades/<int:pk>/excluir/', unidade_delete, name='unidade_delete'),

    path('tiporesiduos/', tipo_residuos['list_view'].as_view(), name='tipos_residuos'),
    path('tipos-residuos/novo/', tipo_residuos['create_view'].as_view(), name='tiporesiduos_create'),
    path('tipos-residuos/<int:pk>/editar/', tipo_residuos['update_view'].as_view(), name='tiporesiduos_update')
]


