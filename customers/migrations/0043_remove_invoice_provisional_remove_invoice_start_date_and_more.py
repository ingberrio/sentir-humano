# Generated by Django 4.0.5 on 2022-06-14 20:13

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0042_customer_is_main_alter_customer_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='provisional',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='start_date',
        ),
        migrations.AddField(
            model_name='invoice',
            name='pay_method',
            field=models.CharField(choices=[('BANCOLOMBIA', 'BANCOLOMBIA'), ('BANCO DE BOG.', 'BANCO DE BOG.'), ('DAVIVIENDA', 'DAVIVIENDA'), ('EFECTIVO', 'EFECTIVO'), ('DATAFONO', 'DATAFONO'), ('OTRO', 'OTRO')], default='DIGITADO', max_length=100, verbose_name='Metodo de pago'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 14, 15, 13, 28, 634147), null=True, verbose_name='Fecha de Suscripcion'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='contribution_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de aporte'),
        ),
    ]