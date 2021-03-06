# Generated by Django 3.1.5 on 2021-06-16 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0007_unidadmedida'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidadmedida',
            options={'verbose_name': 'Unidad de Medida', 'verbose_name_plural': 'Unidades de Medidas'},
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el ')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado el ')),
                ('user_modifc', models.IntegerField(blank=True, null=True)),
                ('codigo', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('codigo_barra', models.CharField(max_length=50)),
                ('precio', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('last_buy', models.DateField(blank=True, null=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.marca')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.subcategory')),
                ('unidadMedida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.unidadmedida')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'unique_together': {('codigo', 'codigo_barra')},
            },
        ),
    ]
