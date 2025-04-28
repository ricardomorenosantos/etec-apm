from django.shortcuts import render
from financeiro.models import Receita, Despesa
from cadastro.models import MembroAPM
from patrimonio.models import Patrimonio
from documentos.models import Ata

def home(request):
    total_receitas = sum(r.valor for r in Receita.objects.all())
    total_despesas = sum(d.valor for d in Despesa.objects.all())
    saldo = total_receitas - total_despesas

    total_membros = MembroAPM.objects.count()
    total_patrimonios = Patrimonio.objects.count()
    total_atas = Ata.objects.count()

    contexto = {
        'saldo': saldo,
        'total_membros': total_membros,
        'total_patrimonios': total_patrimonios,
        'total_atas': total_atas,
    }

    return render(request, 'home.html', contexto)
