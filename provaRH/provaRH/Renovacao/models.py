from django.db import models

class Renovacao(models.Model):
    dataDesocupacao = models.CharField(max_length=20)
    dataRenovacao = models.CharField(max_length=20)
    cartorio = models.CharField(max_length=20)