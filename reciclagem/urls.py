from django.urls import path
from . import views

app_name = 'reciclagem'

urlpatterns = [
    path('ser_recicla/',               views.ser_recicla,     name='ser_recicla_list'),
    path('ser_recicla/editar/<int:pk>/', views.ser_recicla,     name='ser_recicla_edit'),
    path('ser_recicla/excluir/<int:pk>/',views.ser_recicla_delete,name='ser_recicla_delete'),
]