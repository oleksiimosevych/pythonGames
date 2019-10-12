# Generated by Django 2.2.5 on 2019-10-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certification82', '0022_betreiber_projectuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_Generator',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_GeneratorTextmarke',
            field=models.CharField(default='VDE_EZE1_Generator', max_length=100),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_Motor',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_MotorTextmarke',
            field=models.CharField(default='VDE_EZE1_Motor', max_length=100),
        ),
        migrations.AlterField(
            model_name='eze',
            name='VDE_Anzahl_EZE1Textmarke',
            field=models.CharField(default='VDE_Anzahl_EZE1', max_length=100),
        ),
        migrations.AlterField(
            model_name='eze',
            name='VDE_EZE1_HerstTextmarke',
            field=models.CharField(default='VDE_EZE1_Herst', max_length=100),
        ),
        migrations.AlterField(
            model_name='eze',
            name='VDE_EZE1_NameTextmarke',
            field=models.CharField(default='VDE_EZE1_Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='eze',
            name='VDE_EZE1_PTextmarke',
            field=models.CharField(default='VDE_EZE1_P', max_length=100),
        ),
        migrations.AlterField(
            model_name='eze',
            name='VDE_EZE1_STextmarke',
            field=models.CharField(default='VDE_EZE1_S', max_length=100),
        ),
        migrations.AlterField(
            model_name='eze',
            name='VDE_EZE1_TypTextmarke',
            field=models.CharField(default='VDE_EZE1_Typ', max_length=100),
        ),
        migrations.AlterField(
            model_name='eze',
            name='VDE_EZE1_ZertNRTextmarke',
            field=models.CharField(default='VDE_EZE1_ZertNR', max_length=100),
        ),
    ]
