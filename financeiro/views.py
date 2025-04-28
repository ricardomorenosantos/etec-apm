from django.shortcuts import render
from .models import Receita, Despesa
from django.http import HttpResponse

def saldo(request):
    total_receitas = sum(receita.valor for receita in Receita.objects.all())
    total_despesas = sum(despesa.valor for despesa in Despesa.objects.all())
    saldo_final = total_receitas - total_despesas

    return HttpResponse(f"<h1>Saldo atual: R$ {saldo_final:.2f}</h1>")
