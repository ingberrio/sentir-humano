# Generated by Django 3.2.13 on 2022-06-22 21:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20220622_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 22, 16, 43, 6, 473577), null=True, verbose_name='Fecha de Suscripcion'),
        ),
    ]