# Generated by Django 2.2.5 on 2019-09-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification82', '0005_auto_20190915_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ezeneu',
            name='eZeNeu_creation_date',
            field=models.DateTimeField(default='2019-01-01', verbose_name='date published'),
        ),
    ]
