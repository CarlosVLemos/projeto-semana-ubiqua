
from django.urls import path, include
from .views import *
from .forms import *
from utils.generate_view import generate_views

app_name = 'reciclagem'

unidade = generate_views(Unidade, UnidadeForm, 10, template_dir='unidade')
curso = generate_views(Curso, CursoForm, 10, template_dir='curso')
turma = generate_views(Turma, TurmaForm, 10, template_dir='turma')
aluno = generate_views(Aluno, AlunoForm, 10, template_dir='aluno')
tipo_residuos = generate_views(TipoResiduos, TipoResiduosForm, 10, template_dir='tiporesiduos')
reciclagem = generate_views(Reciclagem, ReciclagemForm, 10, template_dir='reciclagem')

urlpatterns = [
    path('unidade/', unidade['list_view'].as_view(), name='unidade_list'),
    path('unidades/novo/', unidade['create_view'].as_view(), name='unidade_create'),
    path('unidades/<int:pk>/editar/', unidade['update_view'].as_view(), name='unidade_update'),
    path('unidades/<int:pk>/excluir/', unidade['delete_view'], name='unidade_delete'),

    path('tiporesiduos/', tipo_residuos['list_view'].as_view(), name='tiporesiduos_list'),
    path('tipos-residuos/novo/', tipo_residuos['create_view'].as_view(), name='tiporesiduos_create'),
    path('tipos-residuos/<int:pk>/editar/', tipo_residuos['update_view'].as_view(), name='tiporesiduos_update'),
    path('tipos-residuos/<int:pk>/excluir/', tipo_residuos['delete_view'], name='tiporesiduos_delete'),

    path('curso/', curso['list_view'].as_view(), name='curso_list'),
    path('cursos/novo/', curso['create_view'].as_view(), name='curso_create'),
    path('cursos/<int:pk>/editar/', curso['update_view'].as_view(), name='curso_update'),
    path('cursos/<int:pk>/excluir/', curso['delete_view'], name='curso_delete'),

    path('turma/', turma['list_view'].as_view(), name='turma_list'),
    path('turmas/novo/', turma['create_view'].as_view(), name='turma_create'),
    path('turmas/<int:pk>/editar/', turma['update_view'].as_view(), name='turma_update'),
    path('turmas/<int:pk>/excluir/', turma['delete_view'], name='turma_delete'),

    path('aluno/', aluno['list_view'].as_view(), name='aluno_list'),
    path('alunos/novo/', aluno['create_view'].as_view(), name='aluno_create'),
    path('alunos/<int:pk>/editar/', aluno['update_view'].as_view(), name='aluno_update'),
    path('alunos/<int:pk>/excluir/', aluno['delete_view'], name='aluno_delete'),

    path('reciclagem/', reciclagem['list_view'].as_view(), name='reciclagem_list'),
    path('reciclagem/novo/', reciclagem['create_view'].as_view(), name='reciclagem_create'),
    path('reciclagem/<int:pk>/editar/', reciclagem['update_view'].as_view(), name='reciclagem_update'),
    path('reciclagem/<int:pk>/excluir/', reciclagem['delete_view'], name='reciclagem_delete'),
]
