# Generated by Django 3.2.13 on 2022-06-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0005_alter_membership_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='value',
            field=models.CharField(max_length=10),
        ),
    ]
