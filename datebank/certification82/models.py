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

class Netzbetreiber(models.Model):
	NB_Ansprech = models.CharField(max_length=250, default='No INFO')
	NB_Name = models.CharField(max_length=250, default='No INFO')
	NB_Str = models.CharField(max_length=250, default='No INFO')
	NB_PLZ = models.CharField(max_length=250, default='No INFO')
	NB_Tel = models.CharField(max_length=250, default='No INFO')
	NB_Fax = models.CharField(max_length=250, default='No INFO')
	NB_Mail = models.CharField(max_length=250, default='No INFO')
	# Textmarke
	NB_AnsprechTextmarke = models.CharField(max_length=250, default='NB_Ansprech')
	NB_NameTextmarke = models.CharField(max_length=250, default='NB_Name')
	NB_StrTextmarke = models.CharField(max_length=250, default='NB_Str')
	NB_PLZTextmarke = models.CharField(max_length=250, default='NB_PLZ')
	NB_TelTextmarke = models.CharField(max_length=250, default='NB_Tel')
	NB_FaxTextmarke = models.CharField(max_length=250, default='NB_Fax')
	NB_MailTextmarke = models.CharField(max_length=250, default='NB_Mail')
	
	def __str__(self):
		return self.NB_Ansprech

class Betreiber(models.Model):
	name = models.CharField(max_length=250, default='No INFO')
	EZA_Betreiber_Anspre = models.CharField(max_length=250, default=' ')
	# EZA_Betreiber_Name = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_StrNr = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_PlzOrt = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_Tel = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_Mail = models.EmailField(max_length=70, blank=True, null=True, unique = True)
	Anlagenzert_Nr = models.CharField(max_length=250, default=' ')

	EZA_Betreiber_AnspreTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Anspre", unique=True)
	EZA_Betreiber_NameTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Name", unique=True)
	EZA_Betreiber_StrNrTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_StrNr", unique=True)
	EZA_Betreiber_PlzOrtTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_PlzOrt", unique=True)
	EZA_Betreiber_TelTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Tel", unique=True)
	EZA_Betreiber_MailTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Mail", unique=True)
	Anlagenzert_NrTextmarke = models.CharField(max_length=100, default="Anlagenzert_Nr", unique=True)

	def __str__(self):
		return self.name

class Zertifikatsinhaber(models.Model):
	#project_id you will select zerfinh in project
	EZA_Bezeichnung  = models.CharField(max_length=250, null=True)
	Zert_Part = models.CharField(max_length=250, null=True)
	Zert_Firm = models.CharField(max_length=250, null=True)
	Zert_Nr = models.CharField(max_length=250, null=True)
	Zert_PLZ = models.CharField(max_length=250, null=True)
	Zert_Tel = models.CharField(max_length=250, null=True)
	Zert_Fax = models.CharField(max_length=250, null=True)
	Zert_Mail = models.EmailField(max_length=70, blank=True, null=True, unique = True)

	EZA_BezeichnungTextmarke = models.CharField(max_length=100, default="EZA_BezeichnungTextmarke")
	Zert_PartTextmarke = models.CharField(max_length=100, default="Zert_Part")
	Zert_FirmTextmarke = models.CharField(max_length=100, default="Zert_Firm")
	Zert_NrTextmarke = models.CharField(max_length=100, default="Zert_Nr")
	Zert_PLZTextmarke = models.CharField(max_length=100, default="Zert_PLZ")
	Zert_TelTextmarke = models.CharField(max_length=100, default="Zert_Tel")
	Zert_FaxTextmarke = models.CharField(max_length=100, default="Zert_Fax")
	Zert_MailTextmarke = models.CharField(max_length=100, default="Zert_Mail")
	def __str__(self):
		return self.EZA_Bezeichnung

class Project(models.Model):
	#ex. windkraft timmendorf 
	project_name = models.CharField(max_length=250) 
	#the number of project --23456
	project_number = models.BigIntegerField(default=0, unique=True)
	#created project at 12 12 19
	project_deadline_date = models.DateField('deadline', null=True)
	#project is done
	is_done = models.BooleanField(default=False)
	access_for_user = models.BooleanField(default=False)
	access_for_moderator = models.BooleanField(default=False)
	access_for_admin = models.BooleanField(default=True)
	#fields
	# Projekt_Nr = models.BigIntegerField(default=0)
	#for project_name
	# Projekttitel = models.CharField(max_length=250, default=' ')
	# Projekt_Date = models.DateField('date published')
	##texmarks
	Projekt_NrTexmarke = models.CharField(max_length=100, default="Projekt_NrN")
	ProjekttitelTexmarke = models.CharField(max_length=100, default="ProjekttitelN")
	Projekt_DateTexmarke = models.CharField(max_length=100, default="Projekt_DateN")	
	Anlagenzert_NrTexmarke = models.CharField(max_length=100, default="Anlagenzert_NrN")
	#link to betreiber
	netzbetreiberTextmarke = models.CharField(max_length=100, default="NB_Ansprech")
	betreiberTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Anspre")
	
	netzbetreiber = models.ForeignKey(Netzbetreiber, on_delete=models.CASCADE, default="", null=True)
	betreiber = models.ForeignKey(Betreiber, on_delete=models.CASCADE, default="", null=True)
	zertifikatsinhaber = models.ForeignKey(Zertifikatsinhaber, on_delete=models.CASCADE, default="", null=True)
	EZA_Betreiber_AnspreTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Anspre")
	Zert_PartTextmarke = models.CharField(max_length=100, default="Zert_Part")

	Registriernummer_NB = models.BigIntegerField(default=0, unique=False, null=True)
	Registriernummer_NBTextmarke = models.CharField(max_length=250, default='Registriernummer_NB')


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
	VDE_EZE1_HerstTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Herst")
	VDE_EZE1_TypTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Typ")
	VDE_EZE1_NameTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Name")
	VDE_EZE1_ZertNRTextmarke = models.CharField(max_length=100, default="VDE_EZE1_ZertNR")
	VDE_EZE1_MotorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Motor")
	VDE_EZE1_GeneratorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Generator")
	VDE_EZE1_STextmarke = models.CharField(max_length=100, default="VDE_EZE1_S")
	VDE_EZE1_PTextmarke = models.CharField(max_length=100, default="VDE_EZE1_P")
	VDE_Anzahl_EZE1Textmarke = models.CharField(max_length=100, default="VDE_Anzahl_EZE1")
	
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
	VDE_TrafoUeberTextmarke = models.CharField(max_length=250, default='VDE_TrafoUeber', unique=True)
	VDE_TrafoOberTextmarke = models.CharField(max_length=250, default='VDE_TrafoOber', unique=True)
	VDE_TrafoUnterTextmarke = models.CharField(max_length=250, default='VDE_TrafoUnter', unique=True)
	VDE_Trafo_kurzTextmarke = models.CharField(max_length=250, default='VDE_Trafo_kurz', unique=True)
	VDE_Trafo_PTextmarke = models.CharField(max_length=250, default='VDE_Trafo_P', unique=True)

	project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)


	def __str__(self):
		return self.VDE_Trafo

################################
#new


	##################################decomment after all created
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

	VDE_EZE_Bestand_ZahlTextmarke = models.CharField(max_length=100,  default="VDE_EZE_Bestand_Zahl")
	VDE_EZE_Herst_AltTextmarke = models.CharField(max_length=100, default="VDE_EZE_Herst_Alt" )
	VDE_EZE_Typ_AltTextmarke = models.CharField(max_length=100, default="VDE_EZE_Typ_Alt" )
	VDE_EZE_Name_ALTTextmarke = models.CharField(max_length=100, default="VDE_EZE_Name_ALT" )
	VDE_S_EZE_AltTextmarke = models.CharField(max_length=100, default="VDE_S_EZE_Alt" )
	VDE_P_EZE_ALTTextmarke = models.CharField(max_length=100, default="VDE_P_EZE_ALT" )
	VDE_P_inbe_ALTTextmarke = models.CharField(max_length=100, default="VDE_P_inbe_ALT" )

	def __str__(self):
		return self.vDE_EZE_Name_ALT


class EzeBestWindkraft(EzeBestand):
	name = models.CharField(max_length=250, default=None)
class EzeBestFotovoltaic(EzeBestand):
	name = models.CharField(max_length=250, default=None)
class EzeBestGenerator(EzeBestand):
	name = models.CharField(max_length=250, default=None)

#####other classes

# class Schutz(models.Model):
# 	"""docstring for Schutz"""
# 	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	

# 	def __str__(self):
# 		return self.name
		
# class Regelung(models.Model):
# 	"""docstring for Regelung"""
# 	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	
# 	def __str__(self):
# 		return self.name


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

