from django.shortcuts import render
from .models import Patrimonio

def listar_patrimonios(request):
    patrimonios = Patrimonio.objects.all().order_by('nome') 
    return render(request, 'patrimonios.html', {'patrimonios': patrimonios})
