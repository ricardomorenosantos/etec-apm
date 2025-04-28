from django.contrib import admin
from .models import MembroAPM

@admin.register(MembroAPM)
class MembroAPMAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cargo', 'cidade', 'telefone')  # Colunas que aparecem no painel
    search_fields = ('nome', 'sobrenome', 'cpf', 'cargo', 'cidade')       # Campos que podem ser buscados
    list_filter = ('cargo', 'cidade', 'estado_civil')                    # Filtros laterais
