# Generated by Django 4.0.5 on 2022-06-08 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0007_supplier_phone_two_alter_supplier_phone'),
        ('customers', '0015_alter_customer_asesor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_appointment', models.CharField(max_length=255, verbose_name='Tipo de cita')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('about', models.TextField(blank=True, max_length=500, verbose_name='Observaciones')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Empleado')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activo')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer', verbose_name='Cliente')),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.supplier', verbose_name='Especialidad')),
            ],
        ),
    ]
