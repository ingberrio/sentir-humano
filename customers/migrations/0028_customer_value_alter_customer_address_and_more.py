# Generated by Django 4.0.5 on 2022-06-10 21:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0027_customer_affiliate_seven_customer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='value',
            field=models.CharField(max_length=20, null=True, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='affiliate_seven_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seven', to='customers.customer', verbose_name='Afiliado Siete'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='affiliate_six_customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='six', to='customers.customer', verbose_name='Afiliado Seis'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 10, 16, 48, 27, 277001), null=True, verbose_name='Fecha de inicio'),
        ),
    ]
