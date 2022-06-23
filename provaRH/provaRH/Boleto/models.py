from django.db import models

class Boleto(models.Model):
    codCliente = models.CharField(max_length=20)
    nomeCliente = models.CharField(max_length=20)