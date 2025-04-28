from django.shortcuts import render
from .models import Ata
from .models import Ata, TermoPosse

def listar_atas(request):
    atas = Ata.objects.all().order_by('-data_reuniao')  # Busca todas as atas, ordenadas da mais recente pra mais antiga
    contexto = {
        'atas': atas
    }
    return render(request, 'atas.html', contexto)

def listar_termos(request):
    termos = TermoPosse.objects.all().order_by('-data_posse')  # Busca todos os termos, mais recentes primeiro
    contexto = {
        'termos': termos
    }
    return render(request, 'termos.html', contexto)