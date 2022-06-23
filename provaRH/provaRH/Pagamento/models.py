from django.db import models

class Pagamento(models.Model):
    valor_pag = models.CharField(max_length=20)
    forma_pag = models.CharField(max_length=20)
    parcelas_pag = models.CharField(max_length=20)
    data_pag = models.CharField(max_length=50)
    banco_pag = models.CharField(max_length=20)
    agencia_pag = models.CharField(max_length=30)
    conta_pag = models.CharField(max_length=20)