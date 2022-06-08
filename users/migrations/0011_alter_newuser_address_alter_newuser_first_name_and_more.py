# Generated by Django 4.0.5 on 2022-06-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_newuser_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='address',
            field=models.CharField(blank=True, default=' ', max_length=150, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]