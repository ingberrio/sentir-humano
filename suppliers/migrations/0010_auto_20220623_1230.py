# Generated by Django 3.2.13 on 2022-06-23 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0009_auto_20220623_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre subcategoria')),
                ('value_sh', models.DecimalField(blank=True, decimal_places=0, default='0', max_digits=10, verbose_name='Valor SH.')),
                ('value', models.DecimalField(blank=True, decimal_places=0, default='0', max_digits=10, verbose_name='Valor particular')),
                ('about', models.TextField(blank=True, null=True, verbose_name='Notas')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updatedAt', models.DateTimeField(verbose_name='Actualizado')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Servicios',
                'verbose_name_plural': 'Servicios',
            },
        ),
        migrations.AddField(
            model_name='supplier',
            name='services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.service', verbose_name='Servicios'),
        ),
    ]
