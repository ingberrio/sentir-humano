# Generated by Django 3.2.13 on 2022-06-23 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0010_auto_20220623_1230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='password',
        ),
    ]
