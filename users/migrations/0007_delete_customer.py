# Generated by Django 4.0.4 on 2022-06-02 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customer_alter_newuser_address_alter_newuser_code_vs_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
