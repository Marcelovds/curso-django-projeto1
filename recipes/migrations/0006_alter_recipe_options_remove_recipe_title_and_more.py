# Generated by Django 4.0 on 2022-03-06 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_options_alter_recipe_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Datalogger', 'verbose_name_plural': 'Dataloggers'},
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='title',
        ),
        migrations.AddField(
            model_name='recipe',
            name='serial_number',
            field=models.CharField(default='test', max_length=65, verbose_name='Número de série'),
            preserve_default=False,
        ),
    ]