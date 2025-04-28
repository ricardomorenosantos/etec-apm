from django.db import models

class Ata(models.Model):
    titulo = models.CharField(max_length=100)
    data_reuniao = models.DateField()
    arquivo = models.FileField(upload_to='atas/')

    def __str__(self):
        return self.titulo

class TermoPosse(models.Model):
    membro_nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)
    data_posse = models.DateField()
    arquivo = models.FileField(upload_to='termos/')

    def __str__(self):
        return f"{self.membro_nome} - {self.cargo}"
