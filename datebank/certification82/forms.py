from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Betreiber
#to add additional fields to user
# class SignUpForm(UserCreationForm):
# 	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
# 	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	
# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

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
	Projekt_Nr = forms.IntegerField(default=0000001)
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
	

	class Meta:
		model = Betreiber
		fields = ('login', 'name', 'EZA_Betreiber_Anspre', 'Projekt_Nr','Projekttitel', 'EZA_Betreiber_Mail', 'EZA_Betreiber_StrNr',\
		 'EZA_Betreiber_PlzOrt', 'EZA_Betreiber_Tel', 'Anlagenzert_Nr', 'password1', 'password2', )