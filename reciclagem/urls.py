
from django.urls import path
from .views import *

app_name = 'reciclagem'


urlpatterns = [
    path('unidades/', UnidadeListView.as_view(), name='unidade_list'),
    path('unidades/novo/', UnidadeCreateView.as_view(), name='unidade_create'),
    path('unidades/<int:pk>/editar/', UnidadeUpdateView.as_view(), name='unidade_update'),
    path('unidades/<int:pk>/excluir/', unidade_delete, name='unidade_delete'),
]


