# Generated by Django 2.0.1 on 2018-01-17 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain', '0011_auto_20180117_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='data',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
