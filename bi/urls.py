from django.urls import path
from .views import *

app_name = 'bi'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/<int:pk>/', DashboardDetailView.as_view(), name='dashboard_detail'),
]
