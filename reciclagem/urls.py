from django.urls import path
from . import views

app_name = 'reciclagem'


urlpatterns = [
    # Unidades
    path('unidades/', views.UnidadeListView.as_view(), name='unidade_list'),
    path('unidades/criar/', views.UnidadeCreateView.as_view(), name='unidade_create'),
    path('unidades/<int:pk>/editar/', views.UnidadeUpdateView.as_view(), name='unidade_update'),
    path('unidades/<int:pk>/excluir/', views.UnidadeDeleteView.as_view(), name='unidade_delete'),

    # Tipos de Resíduo
    path('tipos-residuo/', views.TipoResiduoListView.as_view(), name='tiporesiduo_list'),
    path('tipos-residuo/criar/', views.TipoResiduoCreateView.as_view(), name='tiporesiduo_create'),
    path('tipos-residuo/<int:pk>/editar/', views.TipoResiduoUpdateView.as_view(), name='tiporesiduo_update'),
    path('tipos-residuo/<int:pk>/excluir/', views.TipoResiduoDeleteView.as_view(), name='tiporesiduo_delete'),

    # Reciclagem
    path('reciclagem/', views.ser_recicla, name='ser_recicla_list'),  # alterado para /reciclagem/
    path('reciclagem/criar/', views.ser_recicla, name='ser_recicla_create'),
    path('reciclagem/<int:pk>/', views.ser_recicla, name='ser_recicla_update'),
    path('reciclagem/delete/<int:pk>/', views.ser_recicla_delete, name='ser_recicla_delete'),
]
