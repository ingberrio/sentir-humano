# Generated by Django 4.0.4 on 2022-06-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_remove_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=255, verbose_name='Password'),
        ),
    ]
