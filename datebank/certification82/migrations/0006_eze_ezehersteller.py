# Generated by Django 2.2.5 on 2019-10-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification82', '0005_remove_eze_ezehersteller'),
    ]

    operations = [
        migrations.AddField(
            model_name='eze',
            name='eZeHersteller',
            field=models.CharField(default='N/A', max_length=250),
        ),
    ]
