# Generated by Django 2.0.7 on 2019-08-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190811_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='studentno',
            field=models.CharField(max_length=255),
        ),
    ]
