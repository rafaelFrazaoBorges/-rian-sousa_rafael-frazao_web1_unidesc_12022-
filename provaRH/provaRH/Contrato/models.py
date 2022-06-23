from django.db import models


class Contrato(models.Model):
    dadosCliente = models.CharField(max_length=20)
    dadosCorretor = models.CharField(max_length=20)
    descricaoImovel = models.CharField(max_length=20)
    valor = models.CharField(max_length=50)
    documentacao = models.CharField(max_length=20)
    clausulaPenal = models.CharField(max_length=30)