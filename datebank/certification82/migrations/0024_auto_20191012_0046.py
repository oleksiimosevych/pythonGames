# Generated by Django 2.2.5 on 2019-10-11 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification82', '0023_auto_20191011_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_GeneratorOK',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_MotorOK',
            field=models.BooleanField(default=False),
        ),
    ]
