# Generated by Django 3.2.13 on 2022-06-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0008_alter_supplier_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='discount',
            field=models.CharField(default=' ', max_length=255, verbose_name='Tarifa particular'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone_two',
            field=models.CharField(blank=True, default=' ', max_length=20, verbose_name='Telefono secundario'),
        ),
    ]
