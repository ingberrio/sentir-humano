# Generated by Django 3.2.13 on 2022-06-23 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_alter_customer_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 23, 12, 38, 33, 147830), null=True, verbose_name='Fecha de Suscripcion'),
        ),
    ]
