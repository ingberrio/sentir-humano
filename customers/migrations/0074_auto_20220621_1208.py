# Generated by Django 3.2.13 on 2022-06-21 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0073_alter_customer_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default='', null=True, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 21, 12, 8, 53, 631847), null=True, verbose_name='Fecha de Suscripcion'),
        ),
    ]