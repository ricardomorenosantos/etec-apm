from django.contrib import admin
from .models import Receita, Despesa

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'origem')
    search_fields = ('descricao', 'origem')
    list_filter = ('origem',)

@admin.register(Despesa)
class DespesaAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'data', 'categoria')
    search_fields = ('descricao', 'categoria')
    list_filter = ('categoria',)
