from django.db import models

class Locacao(models.Model):
    dataDesocupacao = models.CharField(max_length=20)
    periodo = models.CharField(max_length=20)
    formaGarantia = models.CharField(max_length=20)
    fiador = models.CharField(max_length=50)