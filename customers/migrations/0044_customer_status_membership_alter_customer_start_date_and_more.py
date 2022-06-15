# Generated by Django 4.0.5 on 2022-06-14 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0043_remove_invoice_provisional_remove_invoice_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='status_membership',
            field=models.CharField(choices=[('COBRO', 'COBRO'), ('PAGO', 'PAGO'), ('INCONVENIENTE', 'INCONVENIENTE'), ('INACTIVO', 'INCATIVO')], default='DIGITADO', max_length=100, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 14, 15, 21, 15, 889680), null=True, verbose_name='Fecha de Suscripcion'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('DIGITADO', 'DIGITADO'), ('CONTABILIZADO', 'CONTABILIZADO'), ('REVISADO', 'REVISADO')], default='DIGITADO', max_length=100, verbose_name='Estado admin'),
        ),
    ]
