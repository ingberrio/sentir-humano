# Generated by Django 4.0.4 on 2022-06-03 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0003_supplier_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='discount',
            field=models.CharField(default=' ', max_length=255, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creado'),
        ),
    ]
