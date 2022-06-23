from django.db import models

class Imovel(models.Model):
    matricula_imo = models.CharField(max_length=20)
    rua_imo = models.CharField(max_length=20)
    cep_imo = models.CharField(max_length=20)
    bairro_imo = models.CharField(max_length=50)
    cidade_imo = models.CharField(max_length=20)
    uf_imo = models.CharField(max_length=30)
    tamanho_imo = models.CharField(max_length=20)
    comodos_imo = models.CharField(max_length=20)
    garagem_imo = models.CharField(max_length=20)
    valor_imo = models.CharField(max_length=20)
    tipo_imo = models.CharField(max_length=20)
    status_imo = models.CharField(max_length=20)