# Generated by Django 2.2.5 on 2019-09-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification82', '0006_auto_20190915_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ezeneu',
            name='eZeNeu_creation_date',
            field=models.DateTimeField(default='NULL', verbose_name='date published'),
        ),
    ]
