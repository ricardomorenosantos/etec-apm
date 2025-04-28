from django.db import models

class Patrimonio(models.Model):
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('em_uso', 'Em uso'),
        ('emprestado', 'Emprestado'),
        ('baixado', 'Baixado'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_aquisicao = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')

    def __str__(self):
        return f"{self.nome} - {self.status}"
