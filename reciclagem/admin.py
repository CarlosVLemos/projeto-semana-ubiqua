from django.contrib import admin
from .models import Unidade, Turma, TipoResiduos, Cidade, Estado, Curso, Reciclagem

admin.site.register(Reciclagem)
admin.site.register(Unidade)
admin.site.register(Turma)
admin.site.register(TipoResiduos)
admin.site.register(Cidade)
admin.site.register(Estado)
admin.site.register(Curso)