from django.db import models


class Gerente(models.Model):
    comissao = models.CharField(max_length=20) #trabalhadores uni-vos!
