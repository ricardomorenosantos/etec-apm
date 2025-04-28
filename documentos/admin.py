from django.contrib import admin
from .models import Ata, TermoPosse

@admin.register(Ata)
class AtaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_reuniao')
    search_fields = ('titulo',)
    list_filter = ('data_reuniao',)

@admin.register(TermoPosse)
class TermoPosseAdmin(admin.ModelAdmin):
    list_display = ('membro_nome', 'cargo', 'data_posse')
    search_fields = ('membro_nome', 'cargo')
    list_filter = ('cargo',)
