from django.contrib import admin
from .models import Patrimonio

@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor', 'data_aquisicao', 'status')
    search_fields = ('nome', 'status')
    list_filter = ('status',)
