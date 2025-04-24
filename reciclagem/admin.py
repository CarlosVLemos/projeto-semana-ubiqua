from django.contrib import admin
from .models import Reciclagem

class ReciclagemAdmin(admin.ModelAdmin):
    list_display  = ('nome','matricula','turma','turno',
                     'semestre','unidade','tipo_residuo',
                     'quantidade','criado_em')
    list_filter   = ('turma','turno','unidade','tipo_residuo')
    search_fields = ('nome','matricula')

admin.site.register(Reciclagem, ReciclagemAdmin)