from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import User
from .models import Dashboard

# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboards = User.objects.get(id=self.request.user.id).dashboards.all()

        context['dashboards'] = dashboards
        
        return context
    
class DashboardDetailView(LoginRequiredMixin, DetailView):
    model = Dashboard
    template_name = 'dashboard_view.html'
    context_object_name = 'dashboard'
