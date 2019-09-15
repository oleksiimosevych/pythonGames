from django.db import models
#for decimal
from decimal import Decimal

class Document(models.Model):
	proofed = models.BooleanField(default=False)
	name = models.CharField(max_length=250)
	comment = models.CharField(max_length=500)
	#file will be saved to MEDIA_ROOT/uploads/2019/11/30
	upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

	def __str__(self):
        return self.name

class Project(models.Model):
	#ex. windkraft timmendorf 
	project_name = models.CharField(max_length=250) 
	#the number of project --23456
	project_number = models.BigIntegerField(default=0)
	#created project at 12 12 19
	project_creation_date = models.DateTimeField('date published')
	#project is done
	is_done = models.BooleanField(default=False)
	access_for_user = models.BooleanField(default=False)
	access_for_moderator = models.BooleanField(default=False)
	access_for_admin = models.BooleanField(default=True)

	def __str__(self):
        return self.project_name

class EzeHersteller(models.Model):
	hersteller_name = models.CharField(max_length=250) 

class EzeTyp(models.Model):
	typ_name = models.CharField(max_length=250)	

class EzeNeu(models.Model):
	#vDE_EZE1_Herst_id
	eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE)
	#vDE_EZE1_Typ_id
	eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE)
	vDE_EZE1_Name = models.CharField(max_length=250)
	vDE_EZE1_ZertNR = models.BigIntegerField(default=0)
	vDE_EZE1_Motor = models.CharField(max_length=250)
	vDE_EZE1_Generator = models.CharField(max_length=250)
	vDE_EZE1_S = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_EZE1_P = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_Anzahl_EZE1 = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))

	def __str__(self):
        return self.vDE_EZE1_Name

class EzeBestand(models.Model):
	vDE_EZE_Bestand_Zahl = models.IntegerField(default=0)
	#vDE_EZE_Herst_Alt_id = //added EZE to Hersteller 13 12
	eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE)
	#vDE_EZE_Typ_Alt_id 
	eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE)
	vDE_EZE_Name_ALT = models.CharField(max_length=250)
	vDE_S_EZE_Alt = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_P_EZE_ALT = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	#jahr
	vDE_P_inbe_ALT = models.IntegerField(default=0)

	def __str__(self):
        return self.vDE_EZE_Name_ALT


# class Proof(models.Model):
# 	projektname = models.CharField(max_length=250)
# 	projektnummer = models.IntegerField(default=0)
# 	dateiname = models.CharField(max_length=250)
# 	vorlage = models.CharField(max_length=500)
# 	speicherpfad = models.CharField(max_length=500)




# class Kategorie(models.Model):
#  	Organisation_id = models.IntegerField(default=0)
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

# class ProofBetrieber(models.Model):
# 	Projektnummer
# 	Projekttitel
# 	Datum
# 	EZA-Betreiber
# 	Ansprechpartner
# 	Str, HausNr.
# 	PLZ, Ort
# 	Telefon
# 	E-Mail
# 	Anlagenzertifikat Nummer

