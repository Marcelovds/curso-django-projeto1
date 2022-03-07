# Generated by Django 4.0.3 on 2022-03-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0007_alter_sensor_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='contrato',
            field=models.CharField(default='contrato', max_length=65),
        ),
        migrations.AddField(
            model_name='sensor',
            name='descricao',
            field=models.CharField(default='Datalogger v1.0', max_length=200),
        ),
        migrations.AddField(
            model_name='sensor',
            name='endereco',
            field=models.CharField(default='Rua', max_length=100),
        ),
        migrations.AddField(
            model_name='sensor',
            name='intervalo_envio',
            field=models.IntegerField(default=15),
        ),
        migrations.AddField(
            model_name='sensor',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sensor',
            name='modelo',
            field=models.CharField(choices=[('Datalogger', 'Datalogger'), ('VRP', 'VRP')], default='Datalogger', max_length=20),
        ),
        migrations.AddField(
            model_name='sensor',
            name='unidade_envio',
            field=models.CharField(default='min', max_length=10),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='slug',
            field=models.SlugField(max_length=65),
        ),
    ]