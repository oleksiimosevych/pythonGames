from django import forms
from decimal import Decimal
# from .forms import UploadFileForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Betreiber, Netzbetreiber, Zertifikatsinhaber, Project, Eze,\
 EzeTyp,EzeHersteller, Document, Transformator, TrafoHersteller, TrafoTyp
#to add additional fields to user
# class SignUpForm(UserCreationForm):
# 	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	
# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class Eze_neu_wind_form(forms.Form):

class NewTrafoHerstellerForm(forms.ModelForm):
	name = forms.CharField(label='Hersteller des Transformators', max_length=250)
	class Meta:
		model =TrafoHersteller
		fields = ('name',)

class NewTrafoTypForm(forms.ModelForm):
	name = forms.CharField(label='Typ des Transformators', max_length=250)
	class Meta:
		model =TrafoTyp 
		fields = ('name',)	

class NewTransformatorForm(forms.ModelForm):
	VDE_TrafoTextmarke = forms.CharField(max_length=250, initial='VDE_Trafo', required=False)
	VDE_TrafoOK = forms.BooleanField(initial=False, required=False)
	VDE_Trafo = forms.CharField(max_length=250, initial='No INFO', required=False)
	
	VDE_TrafoherstellerTextmarke = forms.CharField(max_length=250, initial='VDE_Trafohersteller', required=False)
	VDE_TrafoherstellerOK = forms.BooleanField(initial=False, required=False)
	VDE_Trafohersteller = forms.CharField(max_length=250, initial='Hersteller 1 ', required=False)
	
	VDE_TrafotypTextmarke = forms.CharField(max_length=250, initial='VDE_Trafotyp', required=False)
	VDE_TrafotypOK = forms.BooleanField(initial=False, required=False)
	VDE_Trafotyp = forms.CharField(max_length=250, initial='TYP1', required=False)
	

	VDE_TrafoUeberTextmarke = forms.CharField(max_length=250, initial='VDE_TrafoUeber', required=False)
	VDE_TrafoUeberOK = forms.BooleanField(initial=False, required=False)
	VDE_TrafoUeber = forms.CharField(max_length=250, initial='No INFO', required=False)
	
	VDE_TrafoOberTextmarke = forms.CharField(max_length=250, initial='VDE_TrafoOber', required=False)
	VDE_TrafoOberOK = forms.BooleanField(initial=False, required=False)
	VDE_TrafoOber = forms.DecimalField(max_digits=20,decimal_places=4,initial=Decimal('0.0000'), required=False)
	
	VDE_TrafoUnterTextmarke = forms.CharField(max_length=250, initial='VDE_TrafoUnter', required=False)
	VDE_TrafoUnterOK = forms.BooleanField(initial=False, required=False)
	VDE_TrafoUnter = forms.DecimalField(max_digits=20,decimal_places=4,initial=Decimal('0.0000'), required=False)
	
	VDE_Trafo_kurzTextmarke = forms.CharField(max_length=250, initial='VDE_Trafo_kurz', required=False)
	VDE_Trafo_kurzOK = forms.BooleanField(initial=False, required=False)
	VDE_Trafo_kurz = forms.DecimalField(max_digits=20,decimal_places=4,initial=Decimal('0.0000'), required=False)
	
	VDE_Trafo_PTextmarke = forms.CharField(max_length=250, initial='VDE_Trafo_P', required=False)
	VDE_Trafo_POK = forms.BooleanField(initial=False, required=False)
	VDE_Trafo_P = forms.DecimalField(max_digits=20,decimal_places=4,initial=Decimal('0.0000'), required=False)

	project = forms.ModelChoiceField(label='Projekt', queryset=Project.objects.all())
	class Meta:
		model =Transformator
		fields = ('VDE_TrafoTextmarke','VDE_TrafoOK', 'VDE_Trafo',\
		 'VDE_TrafoherstellerTextmarke','VDE_TrafoherstellerOK','VDE_Trafohersteller',\
		 'VDE_TrafotypTextmarke','VDE_TrafotypOK','VDE_Trafotyp',\
			'VDE_TrafoUeberTextmarke','VDE_TrafoUeberOK','VDE_TrafoUeber',\
			'VDE_TrafoOberTextmarke','VDE_TrafoOberOK','VDE_TrafoOber',\
			'VDE_TrafoUnterTextmarke','VDE_TrafoUnterOK','VDE_TrafoUnter',\
			'VDE_Trafo_kurzTextmarke','VDE_Trafo_kurzOK','VDE_Trafo_kurz',\
			'VDE_Trafo_PTextmarke','VDE_Trafo_POK','VDE_Trafo_P', 'project')

class DateInput(forms.DateInput):
	input_type = 'date'


class NewDocumentForm(forms.ModelForm):

# Verzeichnis hochladen:
	proofed = forms.BooleanField(label='Ist geprüft', initial=False, required=False)
	name = forms.CharField(label='Name', max_length=250)
	comment =forms.CharField(label='Kommentar', max_length=250, widget=forms.Textarea) 
	upload = forms.FileField()
	project = forms.ModelChoiceField(label='Projektname', queryset=Project.objects.all())
	# file = forms.FileField()
	class Meta:
		model =Document
		fields = ('name','comment', 'upload', 'proofed', 'project')

class NewHerstellerForm(forms.ModelForm):
	hersteller_name = forms.CharField(label='Hersteller der EZE', max_length=250)
	class Meta:
		model =EzeHersteller
		fields = ('hersteller_name',)

class NewEzeTypForm(forms.ModelForm):
	typ_name = forms.CharField(label='Typ der EZE', max_length=250)
	class Meta:
		model =EzeTyp 
		fields = ('typ_name',)	

class NewEzeNeuForm(forms.ModelForm):
	eZeHersteller = forms.ModelChoiceField(label='Hersteller der EZE--id', queryset=EzeHersteller.objects.all())
	eZeHerstellerOK = forms.BooleanField(label='OK', required=False)
	#vDE_EZE1_Typ_id
	eZeTyp = forms.ModelChoiceField(queryset=EzeTyp.objects.all())
	project = forms.ModelChoiceField(label='Projekt', queryset=Project.objects.all())
	eZeTypOK = forms.BooleanField(label='OK', required=False)
	#every eze belongs to project
	
	vDE_EZE1_NameOK = forms.BooleanField(label='OK', required=False)
	vDE_EZE1_Name = forms.CharField(label='Bezeichnung der EZE', max_length=250)
	vDE_EZE1_ZertNROK = forms.BooleanField(label='OK', required=False)
	vDE_EZE1_ZertNR = forms.IntegerField(label='Einheitenzertifikat Nr.', required=False)	
	vDE_EZE1_SOK = forms.BooleanField(label='OK', required=False)
	vDE_EZE1_S = forms.DecimalField(label='Bemessungsscheinleistung in MVA', max_digits=20,decimal_places=4,initial=Decimal('0.0000'))
	vDE_EZE1_POK = forms.BooleanField(label='OK', required=False)
	vDE_EZE1_P = forms.DecimalField(label='Bemessungswirkleistung in MW', max_digits=20,decimal_places=4,initial=Decimal('0.0000'))
	vDE_Anzahl_EZE1OK = forms.BooleanField(label='OK', required=False)
	vDE_Anzahl_EZE1 = forms.IntegerField(label='Anzahl der EZE', initial=0)
	VDE_EZE1_HerstTextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_Herst")
	VDE_EZE1_TypTextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_Typ")
	VDE_EZE1_NameTextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_Name")
	VDE_EZE1_ZertNRTextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_ZertNR")
	VDE_EZE1_STextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_S")
	VDE_EZE1_PTextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_P")
	VDE_Anzahl_EZE1Textmarke = forms.CharField(max_length=100, initial="VDE_Anzahl_EZE1")
	
	VDE_EZE1_Motor = forms.CharField(help_text="Für Windkraft und Fotovaltaics leer lassen", max_length=100, required=False, initial='Keine Information')
	VDE_EZE1_Generator = forms.CharField(help_text="Für Windkraft und Fotovaltaics leer lassen", max_length=100, required=False, initial='Keine Information')
	VDE_EZE1_MotorTextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_Motor", required=True)
	VDE_EZE1_GeneratorTextmarke = forms.CharField(max_length=100, initial="VDE_EZE1_Generator", required=True)
	VDE_EZE1_MotorOK = forms.BooleanField(label='OK', required=False)
	VDE_EZE1_GeneratorOK = forms.BooleanField(label='OK', required=False)
	

	ist_bestand = forms.BooleanField(label='Bestand', required=False)


	class Meta:
		model =Eze
		fields = (\
			'eZeHersteller','eZeHerstellerOK','VDE_EZE1_HerstTextmarke',\
			'eZeTyp','eZeTypOK','VDE_EZE1_TypTextmarke','project',\
			'vDE_EZE1_Name','vDE_EZE1_NameOK','VDE_EZE1_NameTextmarke',\
			'vDE_EZE1_ZertNR','vDE_EZE1_ZertNROK','VDE_EZE1_ZertNRTextmarke',\
			'vDE_EZE1_S','vDE_EZE1_SOK','VDE_EZE1_STextmarke',\
			'vDE_EZE1_P','vDE_EZE1_POK','VDE_EZE1_PTextmarke',\
			'vDE_Anzahl_EZE1','vDE_Anzahl_EZE1OK','VDE_Anzahl_EZE1Textmarke',\
			'VDE_EZE1_Motor','VDE_EZE1_MotorOK','VDE_EZE1_MotorTextmarke',\
			'VDE_EZE1_Generator','VDE_EZE1_GeneratorOK','VDE_EZE1_GeneratorTextmarke',\
			'ist_bestand')
class NewEzeBestForm(forms.ModelForm):
	eZeTypOK = forms.BooleanField(label='OK', required=False)
	eZeTyp = forms.ModelChoiceField(label='Typ der EZE', queryset=EzeTyp.objects.all())
	#every eze belongs to project
	project = forms.ModelChoiceField(label='Projektname', queryset=Project.objects.all())
	
	VDE_EZE_Bestand_Zahl = forms.IntegerField(label='Anzahl Bestands-BHKW', initial=0, required = False)
	#vDE_EZE_Herst_Alt_id = //added EZE to Hersteller 13 12
	# EzeHersteller = forms.ForeignKey(EzeHersteller, on_delete=forms.CASCADE)
	#vDE_EZE_Typ_Alt_id 
	# EZeTyp = forms.ForeignKey(EzeTyp, on_delete=forms.CASCADE)
	VDE_EZE_Name_ALT = forms.CharField(label='Bezeichnung der EZE', max_length=250, required = False)
	VDE_S_EZE_Alt = forms.DecimalField(label='Bemessungsscheinleistung in MVA', max_digits=20,decimal_places=4,initial=Decimal('0.0000'), required = False)
	VDE_P_EZE_ALT = forms.DecimalField(label='Bemessungswirkleistung', max_digits=20,decimal_places=4,initial=Decimal('0.0000') , required = False)
	#jahr
	VDE_P_inbe_ALT = forms.IntegerField(label='Inbetriebnahmedatum', initial=2019, required = False)

	VDE_EZE_Bestand_ZahlTextmarke = forms.CharField(max_length=100,  initial="VDE_EZE_Bestand_Zahl")
	#but we still need textmarks
	VDE_EZE_Herst_AltTextmarke = forms.CharField(max_length=100, initial="VDE_EZE_Herst_Alt" )
	eZeHersteller = forms.ModelChoiceField(label='Hersteller der EZE--id', queryset=EzeHersteller.objects.all())
	eZeHerstellerOK = forms.BooleanField(label='OK', required=False)
	
	VDE_EZE_Typ_AltTextmarke = forms.CharField(max_length=100, initial="VDE_EZE_Typ_Alt" )
	VDE_EZE_Name_ALTTextmarke = forms.CharField(max_length=100, initial="VDE_EZE_Name_ALT" )
	VDE_S_EZE_AltTextmarke = forms.CharField(max_length=100, initial="VDE_S_EZE_Alt" )
	VDE_P_EZE_ALTTextmarke = forms.CharField(max_length=100, initial="VDE_P_EZE_ALT" )
	VDE_P_inbe_ALTTextmarke = forms.CharField(max_length=100, initial="VDE_P_inbe_ALT" )
	VDE_EZE_Bestand_ZahlOK = forms.BooleanField(label='OK', required=False)
	#we do not need to double it. I want to optimize code. so.
	# EZeHerstellerOK = forms.BooleanField(label='   ', default=False)
	# EZeTypOK = forms.BooleanField(label='   ', default=False)
	
	VDE_EZE_Name_ALTOK = forms.BooleanField(label='OK', required=False)
	VDE_S_EZE_AltOK = forms.BooleanField(label='OK', required=False)
	VDE_P_EZE_ALTOK = forms.BooleanField(label='OK', required=False)
	VDE_P_inbe_ALTOK = forms.BooleanField(label='OK', required=False)
	ist_bestand = forms.BooleanField(label='Bestand', required=True, initial=True)


	class Meta:
		model =Eze
		fields = ('VDE_EZE_Bestand_Zahl','VDE_EZE_Bestand_ZahlOK','VDE_EZE_Bestand_ZahlTextmarke',\
		 'eZeHersteller', 'eZeHerstellerOK','VDE_EZE_Herst_AltTextmarke',\
			'eZeTyp','eZeTypOK','VDE_EZE_Typ_AltTextmarke',\
			'VDE_EZE_Name_ALT','VDE_EZE_Name_ALTOK','VDE_EZE_Name_ALTTextmarke',\
			'VDE_S_EZE_Alt','VDE_S_EZE_AltOK','VDE_S_EZE_AltTextmarke',\
			'VDE_P_EZE_ALT','VDE_P_EZE_ALTOK','VDE_P_EZE_ALTTextmarke',\
			'VDE_P_inbe_ALT','VDE_P_inbe_ALTOK','VDE_P_inbe_ALTTextmarke',\
			'ist_bestand','project')

class ProjectForm(forms.ModelForm):
	project_name = forms.CharField(max_length=250, required=True, label = 'Projekttitel') 
	project_number = forms.IntegerField(initial=int(245), required=True)
	project_deadline_date = forms.DateField(required=True, widget = DateInput)
	is_done = forms.BooleanField(required=False)
	access_for_user = forms.BooleanField(required=False)
	access_for_moderator = forms.BooleanField(required=False)
	access_for_admin = forms.BooleanField(required=False)
	
	Projekt_NrTexmarke = forms.CharField(max_length=100, initial="Projekt_NrN")
	ProjekttitelTexmarke = forms.CharField(max_length=100, initial="ProjekttitelN")
	Projekt_DateTexmarke = forms.CharField(max_length=100, initial="Projekt_DateN")	
	Anlagenzert_NrTexmarke = forms.CharField(max_length=100, initial="Anlagenzert_NrN")
	netzbetreiberTextmarke = forms.CharField(max_length=100, initial="NB_Ansprech")
	betreiberTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_Anspre")
	
	netzbetreiber = forms.ModelChoiceField(queryset=Netzbetreiber.objects.all())
	betreiber = forms.ModelChoiceField(queryset=Betreiber.objects.all())
	zertifikatsinhaber = forms.ModelChoiceField(queryset=Zertifikatsinhaber.objects.all())

	EZA_Betreiber_AnspreTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_Anspre")
	Zert_PartTextmarke = forms.CharField(max_length=100, initial="Zert_Part")

	Registriernummer_NB = forms.IntegerField(initial=0, required=False)
	Registriernummer_NBTextmarke = forms.CharField(max_length=250, initial='Registriernummer_NB')
	class Meta:
		model = Project
		fields = ('project_name','project_number','project_deadline_date','is_done','access_for_user','access_for_moderator','access_for_admin','Projekt_NrTexmarke'\
			,'ProjekttitelTexmarke','Projekt_DateTexmarke','Anlagenzert_NrTexmarke','netzbetreiberTextmarke','betreiberTextmarke','netzbetreiber','betreiber','zertifikatsinhaber'\
			,'EZA_Betreiber_AnspreTextmarke','Zert_PartTextmarke','Registriernummer_NB','Registriernummer_NBTextmarke')
		widgets = {
		'project_deadline_date': forms.DateInput(attrs={'class':'datepicker'}),
		}


class ZertifikatsinhaberForm(forms.ModelForm):
	EZA_BezeichnungOK = forms.BooleanField(required=False)
	EZA_Bezeichnung  = forms.CharField(max_length=250, required=False)
	Zert_PartOK = forms.BooleanField(required=False)
	Zert_Part = forms.CharField(max_length=250, required=False)
	Zert_FirmOK = forms.BooleanField(required=False)
	Zert_Firm = forms.CharField(max_length=250, required=False)
	Zert_NrOK = forms.BooleanField(required=False)
	Zert_Nr = forms.CharField(max_length=250, required=False)
	Zert_PLZOK = forms.BooleanField(required=False)
	Zert_PLZ = forms.CharField(max_length=250, required=False)
	Zert_TelOK = forms.BooleanField(required=False)
	Zert_Tel = forms.CharField(max_length=250, required=False)
	Zert_FaxOK = forms.BooleanField(required=False)
	Zert_Fax = forms.CharField(max_length=250)
	Zert_MailOK = forms.BooleanField(required=False)
	Zert_Mail = forms.EmailField(max_length=70, required = False)

	EZA_BezeichnungTextmarke = forms.CharField(max_length=100, initial="EZA_BezeichnungTextmarke")
	Zert_PartTextmarke = forms.CharField(max_length=100, initial="Zert_Part")
	Zert_FirmTextmarke = forms.CharField(max_length=100, initial="Zert_Firm")
	Zert_NrTextmarke = forms.CharField(max_length=100, initial="Zert_Nr")
	Zert_PLZTextmarke = forms.CharField(max_length=100, initial="Zert_PLZ")
	Zert_TelTextmarke = forms.CharField(max_length=100, initial="Zert_Tel")
	Zert_FaxTextmarke = forms.CharField(max_length=100, initial="Zert_Fax")
	Zert_MailTextmarke = forms.CharField(max_length=100, initial="Zert_Mail")

	Projekt_Nr = forms.IntegerField(initial=0, required=True)
	Projekt_NrOK=forms.BooleanField(required=False)
	Projekt_NrTextmarke = forms.CharField(max_length=100, initial="Projekt_Nr", required=True)
		

	class Meta:
		model = Zertifikatsinhaber
		fields = ('Projekt_Nr','Projekt_NrOK','EZA_BezeichnungOK','EZA_Bezeichnung','Zert_PartOK','Zert_Part','Zert_FirmOK','Zert_Firm','Zert_NrOK','Zert_Nr'\
			,'Zert_PLZOK','Zert_PLZ','Zert_TelOK','Zert_Tel','Zert_FaxOK','Zert_Fax','Zert_MailOK','Zert_Mail'\
			, 'Projekt_NrTextmarke',\
			 'EZA_BezeichnungTextmarke','Zert_PartTextmarke','Zert_FirmTextmarke','Zert_NrTextmarke','Zert_PLZTextmarke'\
			,'Zert_TelTextmarke','Zert_FaxTextmarke', 'Zert_MailTextmarke')
 

class NetzBetreiberForm(forms.ModelForm):
	Projekt_Nr = forms.IntegerField(initial='', required=True, help_text= 'Please_provide your project NR ')
	Projekt_NrOK=forms.BooleanField(required=False)
	Projekt_NrTextmarke = forms.CharField(max_length=100, initial="Projekt_Nr", required=True)

	NB_AnsprechOK = forms.BooleanField(required=False)
	NB_Ansprech = forms.CharField(label="Netzbetreiber", max_length=100, required=True, help_text='Required.')
	NB_NameOK = forms.BooleanField(required=False)
	NB_Name = forms.CharField(label="Ansprechpartner NB", max_length=100, required=True, help_text='Required. ')
	NB_StrOK = forms.BooleanField(required=False)
	NB_Str = forms.CharField(label="Straße", max_length=100, required=True, help_text='Required. ')
	NB_PLZOK = forms.BooleanField(required=False)
	NB_PLZ = forms.CharField(label="PLZ, Ort", max_length=100, required=True, help_text='Required.')
	NB_TelOK = forms.BooleanField(required=False)
	NB_Tel = forms.CharField(max_length=100 ,required=False, label="Telefon")
	NB_FaxOK = forms.BooleanField(required=False)
	NB_Fax = forms.CharField(required=False, label="Fax")
	NB_MailOK = forms.BooleanField(required=False)
	NB_Mail = forms.EmailField(max_length=255,required=False, label="E-Mail")
	NB_AnsprechTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="NB_Ansprech", required=True)
	NB_NameTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial='NB_NameTextmarke')
	NB_StrTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="NB_Str", required=True)
	NB_PLZTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="NB_PLZ", required=True)
	NB_TelTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="NB_Tel", required=True)
	NB_FaxTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="NB_Fax", required=True)
	NB_MailTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="NB_Mail", required=True)
	#new
	Registriernummer_NB = forms.IntegerField(label="Registrier Nummer NB", required=False, help_text='Additional field')
	Registriernummer_NBTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="Registriernummer_NB", required=True)
	class Meta:
		model = Netzbetreiber
		fields = ('Projekt_Nr','NB_AnsprechOK','NB_Ansprech','NB_NameOK','NB_Name','NB_StrOK','NB_Str','NB_PLZOK','NB_PLZ'\
			,'NB_TelOK','NB_Tel','NB_FaxOK','NB_Fax','NB_MailOK','NB_Mail','Registriernummer_NB','NB_AnsprechTextmarke'\
			,'NB_NameTextmarke','NB_StrTextmarke','NB_PLZTextmarke','NB_TelTextmarke','NB_FaxTextmarke'\
			,'NB_MailTextmarke','Registriernummer_NBTextmarke',\
			'Projekt_NrOK','Projekt_NrTextmarke')
 
class BetreiberForm(forms.ModelForm):
	# first_name = forms.CharField(max_length=100, required=True, help_text='Required. Enter your first name')
	# last_name = forms.CharField(max_length=100, required=True, help_text='Required. Enter your last name.')
	EZA_Betreiber_Mail = forms.EmailField(label="Email", max_length=254, help_text='Required. Inform a valid email address.')
	name = forms.CharField(label="First and Last name", max_length=100, required=True, help_text='Required. Enter your First and Last name here.')
	EZA_Betreiber_Anspre = forms.CharField(label='EZA-Betreiber (Firma)', initial=" GmbH" )
	EZA_Betreiber_StrNr= forms.CharField(label="Street, number", max_length=100, required=True, help_text='Field is required for registration.')
	EZA_Betreiber_PlzOrt = forms.CharField(label="PLZ, Place", max_length=100, required=True, help_text='Field is required for registration.')
	EZA_Betreiber_Tel = forms.CharField(label="Your mobile +49...", max_length=100, required=True, help_text='Field is required for registration.')
	Anlagenzert_Nr = forms.CharField(max_length=100, required=False, help_text='If you do not know what it is contact to your admin.')
	Projekt_Nr = forms.IntegerField(initial='10000001')
	Projekttitel = forms.CharField(max_length=250, required=True, help_text='Field is required for registration.')
	
	Projekt_NrTextmarke = forms.CharField(help_text='Textmarks.', max_length=100, initial="Projekt_Nr", required=True)
	ProjekttitelTextmarke = forms.CharField(max_length=100, initial="Projekttitel", required=True)
	EZA_Betreiber_AnspreTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_Anspre", required=True)
	EZA_Betreiber_NameTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_Name", required=True)
	EZA_Betreiber_StrNrTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_StrNr", required=True)
	EZA_Betreiber_PlzOrtTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_PlzOrt", required=True)
	EZA_Betreiber_TelTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_Tel", required=True)
	EZA_Betreiber_MailTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_Mail", required=True)
	Anlagenzert_NrTextmarke = forms.CharField(max_length=100, initial="Anlagenzert_Nr", required=True)
	login = forms.CharField(max_length=100, initial="name_firma_123", required=True)
	password1 = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)
	nameOK = forms.BooleanField(required=False)
	EZA_Betreiber_AnspreOK = forms.BooleanField(required=False)
	EZA_Betreiber_StrNrOK = forms.BooleanField(required=False)
	EZA_Betreiber_PlzOrtOK = forms.BooleanField(required=False)
	EZA_Betreiber_TelOK = forms.BooleanField(required=False)
	EZA_Betreiber_MailOK = forms.BooleanField(required=False)
	Anlagenzert_NrOK = forms.BooleanField(required=False)
	Projekt_NrOK = forms.BooleanField(required=False)
	ProjekttitelOK = forms.BooleanField(required=False)
	

	class Meta:
		model = Betreiber
		fields = ('login', 'name', 'EZA_Betreiber_Anspre', 'Projekt_Nr',\
			'Projekttitel', 'EZA_Betreiber_Mail', 'EZA_Betreiber_StrNr',\
		 'EZA_Betreiber_PlzOrt', 'EZA_Betreiber_Tel', 'Anlagenzert_Nr', \
		 'password1', 'password2', 'EZA_Betreiber_AnspreOK', 'EZA_Betreiber_StrNrOK',\
		 'EZA_Betreiber_PlzOrtOK','EZA_Betreiber_TelOK','EZA_Betreiber_MailOK',\
		 'Anlagenzert_NrOK','Projekt_NrOK','ProjekttitelOK')