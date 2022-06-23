# Generated by Django 4.0.4 on 2022-06-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pag', models.CharField(max_length=20)),
                ('forma_pag', models.CharField(max_length=20)),
                ('parcelas_pag', models.CharField(max_length=20)),
                ('data_pag', models.CharField(max_length=50)),
                ('banco_pag', models.CharField(max_length=20)),
                ('agencia_pag', models.CharField(max_length=30)),
                ('conta_pag', models.CharField(max_length=20)),
            ],
        ),
    ]
