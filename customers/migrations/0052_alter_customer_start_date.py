# Generated by Django 4.0.5 on 2022-06-15 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0051_alter_customer_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 15, 7, 17, 16, 988088), null=True, verbose_name='Fecha de Suscripcion'),
        ),
    ]
