# Generated by Django 4.0.5 on 2022-06-15 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0063_alter_appointment_end_date_alter_customer_person_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='birth_day',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='start_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 15, 16, 32, 17, 790184), null=True, verbose_name='Fecha de Suscripcion'),
        ),
    ]