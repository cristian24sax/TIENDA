# Generated by Django 3.1.5 on 2021-08-06 16:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0009_auto_20210618_1438'),
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='contact',
            field=models.CharField(max_length=100, verbose_name='Contacto'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='description',
            field=models.CharField(max_length=100, unique=True, verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direction',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefono'),
        ),
        migrations.CreateModel(
            name='ComprasEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
                ('user_modifc', models.IntegerField(blank=True, null=True)),
                ('fecha_compra', models.DateField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('no_factura', models.CharField(max_length=100)),
                ('fecha_factura', models.DateField()),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.proveedor')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Encabezado Compra',
                'verbose_name_plural': 'Encabezado Compras',
            },
        ),
        migrations.CreateModel(
            name='ComprasDet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
                ('user_modifc', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.BigIntegerField(default=0)),
                ('precio_prv', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('costo', models.FloatField(default=0)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.comprasenc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.producto')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Detalle Compra',
                'verbose_name_plural': 'Detalles Compras',
            },
        ),
    ]
