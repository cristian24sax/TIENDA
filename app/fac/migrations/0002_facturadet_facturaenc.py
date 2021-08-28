# Generated by Django 3.1.5 on 2021-08-28 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0009_auto_20210618_1438'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacturaEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.cliente')),
                ('user', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_modifc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Factura',
                'verbose_name_plural': 'Encabezado Facturas',
                'permissions': [('sup_caja_facturaenc', 'Permisos de Supervisor de Caja Encabezado')],
            },
        ),
        migrations.CreateModel(
            name='FacturaDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
                ('cantidad', models.BigIntegerField(default=0)),
                ('precio', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac.facturaenc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.producto')),
                ('user', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_modifc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Factura',
                'verbose_name_plural': 'Detalles Facturas',
                'permissions': [('sup_caja_facturadet', 'Permisos de Supervisor de Caja Detalle')],
            },
        ),
    ]
