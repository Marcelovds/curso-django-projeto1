from distutils.command.upload import upload

from django.db import models


class Sensor(models.Model):
    TEMPERATURA = 'temperatura'
    UMIDADE = 'umidade'
    PRESSAO = 'pressao'
    VAZAO = 'vazao'
    BATERIA = 'bateria'
    DATALOGGER = 'Datalogger'
    VRP = 'VRP'
    contrato = 'contrato'
    endereco = 'endereço'
    descricao = 'descrição'
    intervalo_envio = 15
    unidade_envio = 'min'

    SENSOR_TYPES = [
        (TEMPERATURA, 'Temperatura'),
        (UMIDADE, 'Umidade'),
        (PRESSAO, 'Pressao'),
        (VAZAO, 'Vazao'),
        (BATERIA, 'Bateria')
    ]
    SENSOR_FORMATS = dict([
        (TEMPERATURA, 'temperatura,date'),
        (UMIDADE, 'umidade,date'),
        (PRESSAO, 'pressao,date'),
        (VAZAO, 'vazao,date'),
        (BATERIA, 'bateria,date')
    ])
    SENSOR_MODELOS = [
        (DATALOGGER, 'Datalogger'),
        (VRP, 'VRP')
    ]
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=65)
    type = models.CharField(
        max_length=20,
        choices=SENSOR_TYPES,
        default=PRESSAO,
    )
    modelo = models.CharField(
        max_length=20,
        choices=SENSOR_MODELOS,
        default=DATALOGGER
    )
    contrato = models.CharField(max_length=65, default='contrato')
    endereco = models.CharField(max_length=100, default='Rua')
    descricao = models.CharField(max_length=200, default="Datalogger v1.0")
    intervalo_envio = models.IntegerField(default=15)
    unidade_envio = models.CharField(max_length=10, default='min')
    is_active = models.BooleanField(default=False)

    format = models.CharField(blank=True, max_length=200,
                              help_text="Deixe em branco para deixar no formato padrão (recomendado).")
    creation_date = models.DateTimeField('creation date')

    def save(self, *args, **kwargs):
        if self.format == '':
            self.format = self.SENSOR_FORMATS[self.type]
            super().save(*args, **kwargs)

    def __str__(self):
        return self.name
