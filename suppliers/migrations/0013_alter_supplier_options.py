# Generated by Django 4.0 on 2022-07-26 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0012_auto_20220623_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['-id'], 'verbose_name': 'Proveedores', 'verbose_name_plural': 'Proveedores'},
        ),
    ]
