from django.db import models


class Cheque(models.Model):
    financeira = models.CharField(max_length=20)
    nomeCliente = models.CharField(max_length=20)
    numero = models.CharField(max_length=20)
    dataAbertura = models.CharField(max_length=50)
