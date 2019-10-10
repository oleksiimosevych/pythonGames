from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Betreiber, Netzbetreiber, Zertifikatsinhaber, Project
#to add additional fields to user
# class SignUpForm(UserCreationForm):
# 	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	
# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

# class Eze_neu_wind_form(forms.Form):
class ProjectForm(forms.ModelForm):
	project_name = forms.CharField(max_length=250, required=True, label = 'Projekttitel') 
	project_number = forms.IntegerField(initial=0, required=True)
	project_deadline_date = forms.DateField(required=True)
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

	# /////////
	# netzbetreiber = forms.ChoiceField(
	# 	choices=[(x.id,x.NB_Ansprech) for x in Netzbetreiber.objects.all()]
	# 	)
	# betreiber = forms.ChoiceField(
	# 	choices=[(x.id,x.name) for x in Betreiber.objects.all()]
	# 	)
	# zertifikatsinhaber = forms.ChoiceField(
	# 	choices=[(x.id,x.EZA_Bezeichnung) for x in Zertifikatsinhaber.objects.all()]
	# 	)

	# def save(self, commit=True):
	# 	instance = super().save(commit=False)
	# 	proj_num = self.cleaned_data['project_id']
	# 	instance.netzbetreiber = Netzbetreiber.objects.get(pk=proj_num)
	# 	instance.betreiber = Betreiber.objects.get(pk=proj_num)
	# 	instance.zertifikatsinhaber = Zertifikatsinhaber.objects.get(pk=proj_num)
	# 	instance.save(commit)
	# 	return instance
	# ////////
	
	EZA_Betreiber_AnspreTextmarke = forms.CharField(max_length=100, initial="EZA_Betreiber_Anspre")
	Zert_PartTextmarke = forms.CharField(max_length=100, initial="Zert_Part")

	Registriernummer_NB = forms.IntegerField(initial=0, required=False)
	Registriernummer_NBTextmarke = forms.CharField(max_length=250, initial='Registriernummer_NB')
	class Meta:
		model = Project
		fields = ('project_name','project_number','project_deadline_date','is_done','access_for_user','access_for_moderator','access_for_admin','Projekt_NrTexmarke'\
			,'ProjekttitelTexmarke','Projekt_DateTexmarke','Anlagenzert_NrTexmarke','netzbetreiberTextmarke','betreiberTextmarke','netzbetreiber','betreiber','zertifikatsinhaber'\
			,'EZA_Betreiber_AnspreTextmarke','Zert_PartTextmarke','Registriernummer_NB','Registriernummer_NBTextmarke')


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
