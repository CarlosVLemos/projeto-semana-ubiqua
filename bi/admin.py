from django.contrib import admin
from .models import *

# Register your models here.
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link')

admin.site.register(Dashboard, DashboardAdmin)