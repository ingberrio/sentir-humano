# Generated by Django 4.0.4 on 2022-06-04 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0004_supplier_discount_alter_supplier_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='city',
            field=models.CharField(default='', max_length=255, verbose_name='Especialidad'),
        ),
    ]
