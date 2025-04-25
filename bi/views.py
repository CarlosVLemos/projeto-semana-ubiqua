from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from .models import Dashboard
from reciclagem.models import Reciclagem, Unidade, TipoResiduos, Turma
from django.db.models import Sum
import json

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        unidades = Unidade.objects.all()
        tipos_residuos = TipoResiduos.objects.all()
        turmas = Turma.objects.all()

        total_por_tipo_material = {}
        for tipo in tipos_residuos:
            #total por tipo de material
            total = Reciclagem.objects.filter(tipo_residuo=tipo).aggregate(Sum('quantidade'))['quantidade__sum']
            if total is None:
                total = 0
            total_por_tipo_material[tipo.nome] = total

        total_por_unidades = {}
        for unidade in unidades:
            #total por unidade
            total = Reciclagem.objects.filter(aluno__turma__curso__unidade=unidade).aggregate(Sum('quantidade'))['quantidade__sum']
            if total is None:
                total = 0
            total_por_unidades[unidade.nome] = total

        total_por_turma = {}
        for turma in turmas:
            total = Reciclagem.objects.filter(aluno__turma=turma).aggregate(Sum('quantidade'))['quantidade__sum']
            if total is None:
                total = 0
            total_por_turma[f'{turma.nome} - {turma.curso}'] = total

        #evolução por mes
        total_por_mes = Reciclagem.objects.values('data__year', 'data__month').annotate(total=Sum('quantidade')).order_by('data__year', 'data__month')
        total_por_mes = {f"{item['data__year']}-{item['data__month']}": item['total'] for item in total_por_mes}


        context['labels'] = json.dumps(list(total_por_unidades.keys()))
        context['values'] = json.dumps(list(total_por_unidades.values()))

        context['labels_tipo'] = json.dumps(list(total_por_tipo_material.keys()))
        context['values_tipo'] = json.dumps(list(total_por_tipo_material.values()))

        context['labels_turma'] = json.dumps(list(total_por_turma.keys()))
        context['values_turma'] = json.dumps(list(total_por_turma.values()))

        context['labels_mes'] = json.dumps(list(total_por_mes.keys()))
        context['values_mes'] = json.dumps(list(total_por_mes.values()))
        
        return context
    
class DashboardDetailView(LoginRequiredMixin, DetailView):
    model = Dashboard
    template_name = 'dashboard_view.html'
    context_object_name = 'dashboard'
