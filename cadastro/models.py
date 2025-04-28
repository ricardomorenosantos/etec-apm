from django.db import models

class MembroAPM(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    cargo = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=20)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"
