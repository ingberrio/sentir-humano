# Generated by Django 3.2.13 on 2022-06-23 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0011_remove_service_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='services',
        ),
        migrations.AddField(
            model_name='service',
            name='suppliers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='suppliers.supplier', verbose_name='Servicios'),
        ),
        migrations.AlterField(
            model_name='service',
            name='updatedAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Actualizado'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Direccion'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Notas'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='discount',
            field=models.CharField(blank=True, default=' ', max_length=255, verbose_name='Tarifa particular'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]