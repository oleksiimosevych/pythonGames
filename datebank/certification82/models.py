from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Category(models.Model):
	category_name = models.CharField(max_length=200)

class Proof(models.Model):
	projektname = models.CharField(max_length=250)
	projektnummer = models.IntegerField(default=0)
	dateiname = models.CharField(max_length=250)
	vorlage = models.CharField(max_length=500)
	speicherpfad = models.CharField(max_length=500)

class Kategorie(models.Model):
 	Organisation_id = models.IntegerField(default=0)
# 	Betreiber
# 	Zertifikatsinhaber
# 	Netzbetreiber
# 	Netzbetreiberbogen
# 	Distanzschutz NAP
# 	Überstromzeitschutz NAP
# 	Erdschlussschutz NAP
# 	Spannungssteigerungsschutz NAP
# 	Spannungsrückgangsschutz NAP
# 	Frequenzstei-gerungsschutz NAP
# 	Frequenzrück-gangsschutz NAP
# 	Blindleistungsunter-spannungsschutz NAP
# 	Spannungssteigerungs-schutz EZE
# 	Spannungsrückgangs-schutz EZE
# 	Frequenz-steigerungs-schutz EZE
# 	Frequenz-rückgangsschutz EZE
# 	Blindleistungsunter-spannungsschutz EZE
# 	Schutzprüf-protokolle
# 	SLD
# 	Kommunikationsplan
# 	EZE-Typ Neu
# 	EZE-Typ Neu
# 	Weitere EZE-Bestand
# 	Weitere EZE-Bestand
# 	Weitere EZE-Bestand
# 	Weitere EZE-Alt
# 	Weitere EZE-Alt
# 	Weitere EZE-Alt
# 	Spannungsänderungen
# 	Ordnung
# 	Frequenz in Hz
# 	Errechneter ges. Strom in A
# 	Zulässiger ges. Strom in A
# 	Ergebnis

class ProofBetrieber(models.Model):
	Projektnummer
	Projekttitel
	Datum
	EZA-Betreiber
	Ansprechpartner
	Str, HausNr.
	PLZ, Ort
	Telefon
	E-Mail
	Anlagenzertifikat Nummer

