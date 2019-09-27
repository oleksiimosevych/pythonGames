from django.db import models
#for decimal
from decimal import Decimal
from django.utils import timezone
#please use only TAB not spaces...
class Document(models.Model):
	proofed = models.BooleanField(default=False)
	name = models.CharField(max_length=250)
	comment = models.CharField(max_length=500)
	#file will be saved to MEDIA_ROOT/uploads/2019/11/30
	upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

	def __str__(self):
		return self.name

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

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
	#fields
	# Projekt_Nr
	# Projekttitel
	# Projekt_Date
	# EZA_Betreiber_Anspre
	# EZA_Betreiber_Name
	# EZA_Betreiber_StrNr
	# EZA_Betreiber_PlzOrt
	# EZA_Betreiber_Tel
	# EZA_Betreiber_Mail
	# Anlagenzert_Nr
	##texmarks
	Projekt_NrTexmarke = models.CharField(max_length=100, default="Projekt_NrN", unique=True)
	ProjekttitelTexmarke = models.CharField(max_length=100, default="ProjekttitelN", unique=True)
	Projekt_DateTexmarke = models.CharField(max_length=100, default="Projekt_DateN", unique=True)
	EZA_Betreiber_AnspreTexmarke = models.CharField(max_length=100, default="EZA_Betreiber_AnspreN", unique=True)
	EZA_Betreiber_NameTexmarke = models.CharField(max_length=100, default="EZA_Betreiber_NameN", unique=True)
	EZA_Betreiber_StrNrTexmarke = models.CharField(max_length=100, default="EZA_Betreiber_StrNrN", unique=True)
	EZA_Betreiber_PlzOrtTexmarke = models.CharField(max_length=100, default="EZA_Betreiber_PlzOrtN", unique=True)
	EZA_Betreiber_TelTexmarke = models.CharField(max_length=100, default="EZA_Betreiber_TelN", unique=True)
	EZA_Betreiber_MailTexmarke = models.CharField(max_length=100, default="EZA_Betreiber_MailN", unique=True)
	Anlagenzert_NrTexmarke = models.CharField(max_length=100, default="Anlagenzert_NrN", unique=True)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.project_name

class EzeHersteller(models.Model):
	hersteller_name = models.CharField(max_length=250) 
	def __str__(self):
		return self.hersteller_name
class EzeTyp(models.Model):
	typ_name = models.CharField(max_length=250)	
	def __str__(self):
		return self.typ_name


class EzeNeu(models.Model):
	#vDE_EZE1_Herst_id
	eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE, default=None)
	#vDE_EZE1_Typ_id
	eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE, default=1)
	#every eze belongs to project
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	vDE_EZE1_Name = models.CharField(max_length=250)
	vDE_EZE1_ZertNR = models.BigIntegerField(default=0)	
	vDE_EZE1_S = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_EZE1_P = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_Anzahl_EZE1 = models.IntegerField(default=0)
	#not for wind and foto
	vDE_EZE1_Motor = models.CharField(max_length=250)
	vDE_EZE1_Generator = models.CharField(max_length=250)
	##TEXTMARKEN
	# eZeNeu_creation_date = models.DateField('date published', default='2019-01-01')
	VDE_EZE1_HerstTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Herst", unique=True)
	VDE_EZE1_TypTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Typ", unique=True)
	VDE_EZE1_NameTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Name", unique=True)
	VDE_EZE1_ZertNRTextmarke = models.CharField(max_length=100, default="VDE_EZE1_ZertNR", unique=True)
	VDE_EZE1_MotorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Motor", unique=True)
	VDE_EZE1_GeneratorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Generator", unique=True)
	VDE_EZE1_STextmarke = models.CharField(max_length=100, default="VDE_EZE1_S", unique=True)
	VDE_EZE1_PTextmarke = models.CharField(max_length=100, default="VDE_EZE1_P", unique=True)
	VDE_Anzahl_EZE1Textmarke = models.CharField(max_length=100, default="VDE_Anzahl_EZE1", unique=True)
	
	def __str__(self):
		return self.vDE_EZE1_Name

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Eze(models.Model):
	#vDE_EZE1_Herst_id
	eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE, default=None)
	#vDE_EZE1_Typ_id
	eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE, default=1)
	#every eze belongs to project
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	vDE_EZE1_Name = models.CharField(max_length=250)
	vDE_EZE1_ZertNR = models.BigIntegerField(default=0)	
	vDE_EZE1_S = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_EZE1_P = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_Anzahl_EZE1 = models.IntegerField(default=0)
	# eZeNeu_creation_date = models.DateField('date published', default='2019-01-01')
	VDE_EZE1_HerstTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Herst", unique=True)
	VDE_EZE1_TypTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Typ", unique=True)
	VDE_EZE1_NameTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Name", unique=True)
	VDE_EZE1_ZertNRTextmarke = models.CharField(max_length=100, default="VDE_EZE1_ZertNR", unique=True)
	VDE_EZE1_STextmarke = models.CharField(max_length=100, default="VDE_EZE1_S", unique=True)
	VDE_EZE1_PTextmarke = models.CharField(max_length=100, default="VDE_EZE1_P", unique=True)
	VDE_Anzahl_EZE1Textmarke = models.CharField(max_length=100, default="VDE_Anzahl_EZE1", unique=True)

	def __str__(self):
		return self.vDE_EZE1_Name


class EzeNeuWindkraft(Eze):
	name = models.CharField(max_length=250, default=None)
	def __str__(self):
		return self.name
class EzeNeuFotovoltaic(Eze):
	name = models.CharField(max_length=250, default=None)
	def __str__(self):
		return self.name
class EzeNeuGenerator(EzeNeu):
	name = models.CharField(max_length=250, default=None)
	def __str__(self):
		return self.name

class TrafoHersteller(models.Model):
	name = models.CharField(max_length=250, default='No INFO')
	def __str__(self):
		return self.name

class TrafoTyp(models.Model):
	name = models.CharField(max_length=250, default='No INFO')
	def __str__(self):
		return self.name


class Transformator(models.Model):
	VDE_Trafo = models.CharField(max_length=250, default='No INFO')
	VDE_Trafohersteller = models.ForeignKey(TrafoHersteller, on_delete=models.CASCADE, default='No INFO')
	VDE_Trafotyp = models.ForeignKey(TrafoTyp, on_delete=models.CASCADE, default='No INFO')
	VDE_TrafoUeber = models.CharField(max_length=250, default='No INFO')
	VDE_TrafoOber = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	VDE_TrafoUnter = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	VDE_Trafo_kurz = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	VDE_Trafo_P = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))

	VDE_TrafoTextmarke = models.CharField(max_length=250, default='VDE_Trafo', unique=True)
	VDE_TrafoherstellerTextmarke = models.CharField(max_length=250, default='VDE_Trafohersteller', unique=True)
	VDE_TrafotypTextmarke = models.CharField(max_length=250, default='VDE_Trafotyp', unique=True)
	VDE_TrafoUeberTextmarke = models.CharField(max_length=250, default='VDE_TrafoÜber', unique=True)
	VDE_TrafoOberTextmarke = models.CharField(max_length=250, default='VDE_TrafoOber', unique=True)
	VDE_TrafoUnterTextmarke = models.CharField(max_length=250, default='VDE_TrafoUnter', unique=True)
	VDE_Trafo_kurzTextmarke = models.CharField(max_length=250, default='VDE_Trafo_kurz', unique=True)
	VDE_Trafo_PTextmarke = models.CharField(max_length=250, default='VDE_Trafo_P', unique=True)

	def __str__(self):
		return self.VDE_Trafo

################################
#new
class Betreiber(models.Model):
	name = models.CharField(max_length=250, default='No INFO')
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	Projekt_Nr = models.BigIntegerField(default=0)
	Projekttitel = models.CharField(max_length=250, default=' ')
	Projekt_Date = models.DateTimeField('date published')
	EZA_Betreiber_Anspre = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_Name = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_StrNr = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_PlzOrt = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_Tel = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_Mail = models.EmailField(max_length=70, blank=True, null=True, unique = True)
	Anlagenzert_Nr = models.CharField(max_length=250, default=' ')

	Projekt_NrTextmarke = models.CharField(max_length=100, default="Projekt_Nr", unique=True)
	ProjekttitelTextmarke = models.CharField(max_length=100, default="Projekttitel", unique=True)
	Projekt_DateTextmarke = models.CharField(max_length=100, default="Projekt_Date", unique=True)
	EZA_Betreiber_AnspreTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Anspre", unique=True)
	EZA_Betreiber_NameTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Name", unique=True)
	EZA_Betreiber_StrNrTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_StrNr", unique=True)
	EZA_Betreiber_PlzOrtTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_PlzOrt", unique=True)
	EZA_Betreiber_TelTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Tel", unique=True)
	EZA_Betreiber_MailTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Mail", unique=True)
	Anlagenzert_NrTextmarke = models.CharField(max_length=100, default="Anlagenzert_Nr", unique=True)

	def __str__(self):
		return self.name

class Schutz(models.Model):
	"""docstring for Schutz"""
	def __str__(self):
		return self.name
		
class Regelung(models.Model):
	"""docstring for Regelung"""
	def __str__(self):
		return self.name

##################################decomment after all created


# class EzeNeu_Generator(models.Model):
# 	eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE)
# 	#vDE_EZE1_Typ_id
# 	eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE)
# 	#every eze belongs to project
# 	project = models.ForeignKey(Project, on_delete=models.CASCADE)
# 	vDE_EZE1_Name = models.CharField(max_length=250)
# 	vDE_EZE1_ZertNR = models.BigIntegerField(default=0)
# 	vDE_EZE1_S = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
# 	vDE_EZE1_P = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
# 	vDE_Anzahl_EZE1 = models.IntegerField(default=0)
	
# 	name = models.CharField(max_length=250)
# 	vDE_EZE1_Motor = models.CharField(max_length=250)
# 	vDE_EZE1_Generator = models.CharField(max_length=250)
# 	def __str__(self):
# 		return self.name



class EzeBestand(models.Model):
	#every ezebestand belongs to a specific Project
	project = models.ForeignKey(Project, on_delete=models.CASCADE)

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


class EzeBestWindkraft(EzeBestand):
	name = models.CharField(max_length=250, default=None)
class EzeBestFotovoltaic(EzeBestand):
	name = models.CharField(max_length=250, default=None)
class EzeBestGenerator(EzeBestand):
	name = models.CharField(max_length=250, default=None)

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

