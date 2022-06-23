from django.db import models

class Pessoa(models.Model):
    matricula = models.CharField(max_length=5)
    telefone = models.CharField(max_length=13)
    cep = models.CharField(max_length=8)
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=30)
    uf = models.CharField(max_length=2)