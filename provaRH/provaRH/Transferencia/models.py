from django.db import models


class Transferencia(models.Model):
    tipo = models.CharField(max_length=20)
    codIdentificacao = models.CharField(max_length=20)