# Generated by Django 2.2.5 on 2019-09-15 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certification82', '0002_auto_20190915_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ezebestand',
            old_name='eZehersteller',
            new_name='eZeHersteller',
        ),
    ]
