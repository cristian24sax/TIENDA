# Generated by Django 3.1.5 on 2021-05-31 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0002_remove_category_updated_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='user_modifc',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
