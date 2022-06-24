# Generated by Django 3.2.13 on 2022-06-23 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city_pay',
            field=models.CharField(blank=True, choices=[('ARMENIA', 'ARMENIA'), ('CARTAGO', 'CARTAGO'), ('QUIMBAYA', 'QUIMBAYA'), ('PEREIRA', 'PEREIRA')], default=' ', max_length=20, verbose_name='Ciudad'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_contact',
            field=models.CharField(blank=True, max_length=20, verbose_name='Telefono de contacto'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, choices=[('ARMENIA', 'ARMENIA'), ('CARTAGO', 'CARTAGO'), ('QUIMBAYA', 'QUIMBAYA'), ('PEREIRA', 'PEREIRA')], default=' ', max_length=20, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefono'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 23, 10, 35, 17, 863403), null=True, verbose_name='Fecha de Suscripcion'),
        ),
    ]
