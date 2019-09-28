# Generated by Django 2.2.5 on 2019-09-28 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certification82', '0002_trafohersteller_trafotyp_transformator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betreiber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No INFO', max_length=250)),
                ('EZA_Betreiber_Anspre', models.CharField(default=' ', max_length=250)),
                ('EZA_Betreiber_StrNr', models.CharField(default=' ', max_length=250)),
                ('EZA_Betreiber_PlzOrt', models.CharField(default=' ', max_length=250)),
                ('EZA_Betreiber_Tel', models.CharField(default=' ', max_length=250)),
                ('EZA_Betreiber_Mail', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('Anlagenzert_Nr', models.CharField(default=' ', max_length=250)),
                ('EZA_Betreiber_AnspreTextmarke', models.CharField(default='EZA_Betreiber_Anspre', max_length=100, unique=True)),
                ('EZA_Betreiber_NameTextmarke', models.CharField(default='EZA_Betreiber_Name', max_length=100, unique=True)),
                ('EZA_Betreiber_StrNrTextmarke', models.CharField(default='EZA_Betreiber_StrNr', max_length=100, unique=True)),
                ('EZA_Betreiber_PlzOrtTextmarke', models.CharField(default='EZA_Betreiber_PlzOrt', max_length=100, unique=True)),
                ('EZA_Betreiber_TelTextmarke', models.CharField(default='EZA_Betreiber_Tel', max_length=100, unique=True)),
                ('EZA_Betreiber_MailTextmarke', models.CharField(default='EZA_Betreiber_Mail', max_length=100, unique=True)),
                ('Anlagenzert_NrTextmarke', models.CharField(default='Anlagenzert_Nr', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Zertifikatsinhaber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EZA_Bezeichnung', models.CharField(max_length=250, null=True)),
                ('Zert_Part', models.CharField(max_length=250, null=True)),
                ('Zert_Firm', models.CharField(max_length=250, null=True)),
                ('Zert_Nr', models.CharField(max_length=250, null=True)),
                ('Zert_PLZ', models.CharField(max_length=250, null=True)),
                ('Zert_Tel', models.CharField(max_length=250, null=True)),
                ('Zert_Fax', models.CharField(max_length=250, null=True)),
                ('Zert_Mail', models.EmailField(blank=True, max_length=70, null=True, unique=True)),
                ('EZA_BezeichnungTextmarke', models.CharField(default='EZA_BezeichnungTextmarke', max_length=100)),
                ('Zert_PartTextmarke', models.CharField(default='Zert_Part', max_length=100)),
                ('Zert_FirmTextmarke', models.CharField(default='Zert_Firm', max_length=100)),
                ('Zert_NrTextmarke', models.CharField(default='Zert_Nr', max_length=100)),
                ('Zert_PLZTextmarke', models.CharField(default='Zert_PLZ', max_length=100)),
                ('Zert_TelTextmarke', models.CharField(default='Zert_Tel', max_length=100)),
                ('Zert_FaxTextmarke', models.CharField(default='Zert_Fax', max_length=100)),
                ('Zert_MailTextmarke', models.CharField(default='Zert_Mail', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_creation_date',
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_Anzahl_EZE1Textmarke',
            field=models.CharField(default='VDE_Anzahl_EZE1', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_HerstTextmarke',
            field=models.CharField(default='VDE_EZE1_Herst', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_NameTextmarke',
            field=models.CharField(default='VDE_EZE1_Name', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_PTextmarke',
            field=models.CharField(default='VDE_EZE1_P', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_STextmarke',
            field=models.CharField(default='VDE_EZE1_S', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_TypTextmarke',
            field=models.CharField(default='VDE_EZE1_Typ', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='eze',
            name='VDE_EZE1_ZertNRTextmarke',
            field=models.CharField(default='VDE_EZE1_ZertNR', max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='ezebestand',
            name='VDE_EZE_Bestand_ZahlTextmarke',
            field=models.CharField(default='VDE_EZE_Bestand_Zahl', max_length=100),
        ),
        migrations.AddField(
            model_name='ezebestand',
            name='VDE_EZE_Herst_AltTextmarke',
            field=models.CharField(default='VDE_EZE_Herst_Alt', max_length=100),
        ),
        migrations.AddField(
            model_name='ezebestand',
            name='VDE_EZE_Name_ALTTextmarke',
            field=models.CharField(default='VDE_EZE_Name_ALT', max_length=100),
        ),
        migrations.AddField(
            model_name='ezebestand',
            name='VDE_EZE_Typ_AltTextmarke',
            field=models.CharField(default='VDE_EZE_Typ_Alt', max_length=100),
        ),
        migrations.AddField(
            model_name='ezebestand',
            name='VDE_P_EZE_ALTTextmarke',
            field=models.CharField(default='VDE_P_EZE_ALT', max_length=100),
        ),
        migrations.AddField(
            model_name='ezebestand',
            name='VDE_P_inbe_ALTTextmarke',
            field=models.CharField(default='VDE_P_inbe_ALT', max_length=100),
        ),
        migrations.AddField(
            model_name='ezebestand',
            name='VDE_S_EZE_AltTextmarke',
            field=models.CharField(default='VDE_S_EZE_Alt', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_Anzahl_EZE1Textmarke',
            field=models.CharField(default='VDE_Anzahl_EZE1', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_GeneratorTextmarke',
            field=models.CharField(default='VDE_EZE1_Generator', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_HerstTextmarke',
            field=models.CharField(default='VDE_EZE1_Herst', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_MotorTextmarke',
            field=models.CharField(default='VDE_EZE1_Motor', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_NameTextmarke',
            field=models.CharField(default='VDE_EZE1_Name', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_PTextmarke',
            field=models.CharField(default='VDE_EZE1_P', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_STextmarke',
            field=models.CharField(default='VDE_EZE1_S', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_TypTextmarke',
            field=models.CharField(default='VDE_EZE1_Typ', max_length=100),
        ),
        migrations.AddField(
            model_name='ezeneu',
            name='VDE_EZE1_ZertNRTextmarke',
            field=models.CharField(default='VDE_EZE1_ZertNR', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='Anlagenzert_NrTexmarke',
            field=models.CharField(default='Anlagenzert_NrN', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='Projekt_DateTexmarke',
            field=models.CharField(default='Projekt_DateN', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='Projekt_NrTexmarke',
            field=models.CharField(default='Projekt_NrN', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='ProjekttitelTexmarke',
            field=models.CharField(default='ProjekttitelN', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='project_deadline_date',
            field=models.DateField(null=True, verbose_name='deadline'),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_TrafoOberTextmarke',
            field=models.CharField(default='VDE_TrafoOber', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_TrafoTextmarke',
            field=models.CharField(default='VDE_Trafo', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_TrafoUeberTextmarke',
            field=models.CharField(default='VDE_TrafoUeber', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_TrafoUnterTextmarke',
            field=models.CharField(default='VDE_TrafoUnter', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_Trafo_PTextmarke',
            field=models.CharField(default='VDE_Trafo_P', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_Trafo_kurzTextmarke',
            field=models.CharField(default='VDE_Trafo_kurz', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_TrafoherstellerTextmarke',
            field=models.CharField(default='VDE_Trafohersteller', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='VDE_TrafotypTextmarke',
            field=models.CharField(default='VDE_Trafotyp', max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='transformator',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='certification82.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_number',
            field=models.BigIntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='project',
            name='betreiber',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='certification82.Betreiber'),
        ),
        migrations.AddField(
            model_name='project',
            name='zertifikatsinhaber',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='certification82.Zertifikatsinhaber'),
        ),
    ]
