# Generated by Django 4.0.4 on 2022-06-22 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Renovacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataDesocupacao', models.CharField(max_length=20)),
                ('dataRenovacao', models.CharField(max_length=20)),
                ('cartorio', models.CharField(max_length=20)),
            ],
        ),
    ]
