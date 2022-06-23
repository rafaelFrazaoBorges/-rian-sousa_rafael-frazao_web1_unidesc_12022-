from django.db import models


class Corretor(models.Model):
    comissao = models.CharField(max_length=20)
    idCorretor = models.CharField(max_length=20)