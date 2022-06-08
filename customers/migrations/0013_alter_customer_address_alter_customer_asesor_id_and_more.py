# Generated by Django 4.0.5 on 2022-06-07 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0012_alter_customer_membership_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='asesor_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Asesor encargado'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Notas'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telefono'),
        ),
    ]