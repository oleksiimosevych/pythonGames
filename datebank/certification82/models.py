from django.db import models
#for decimal
from decimal import Decimal
from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, User, AbstractBaseUser
from datebank import settings

# from django.contrib.auth.models import  AbstractBaseUser
#please use only TAB not spaces...

class User2(AbstractBaseUser):
	pass
#D
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
	def get_absolute_url(self):
		return reverse('certification82:documentdetailview', kwargs={'pk': self.pk})
#N
class Netzbetreiber(models.Model):
	NB_AnsprechOK=models.BooleanField(default=False)
	NB_Ansprech = models.CharField(max_length=250, default='No INFO')
	NB_NameOK=models.BooleanField(default=False)
	NB_Name = models.CharField(max_length=250, default='No INFO')
	NB_StrOK=models.BooleanField(default=False)
	NB_Str = models.CharField(max_length=250, default='No INFO')
	NB_PLZOK=models.BooleanField(default=False)
	NB_PLZ = models.CharField(max_length=250, default='No INFO')
	NB_TelOK=models.BooleanField(default=False)
	NB_Tel = models.CharField(max_length=250, default='No INFO')
	NB_FaxOK=models.BooleanField(default=False)
	NB_Fax = models.CharField(max_length=250, default='No INFO')
	NB_MailOK=models.BooleanField(default=False)
	NB_Mail = models.EmailField(max_length=250, default='a@b.dfg')
	# Textmarke
	NB_AnsprechTextmarke = models.CharField(max_length=250, default='NB_Ansprech')
	NB_NameTextmarke = models.CharField(max_length=250, default='NB_Name')
	NB_StrTextmarke = models.CharField(max_length=250, default='NB_Str')
	NB_PLZTextmarke = models.CharField(max_length=250, default='NB_PLZ')
	NB_TelTextmarke = models.CharField(max_length=250, default='NB_Tel')
	NB_FaxTextmarke = models.CharField(max_length=250, default='NB_Fax')
	NB_MailTextmarke = models.CharField(max_length=250, default='NB_Mail')
	Registriernummer_NB = models.BigIntegerField(default=0, null=True)
	Registriernummer_NBTextmarke = models.CharField(max_length=250, default='Registriernummer_NB')
	Projekt_Nr = models.BigIntegerField(default=0, unique=False)
	Projekt_NrOK=models.BooleanField(default=False)
	Registriernummer_NBOK=models.BooleanField(default=False)
	Projekt_NrTextmarke = models.CharField(max_length=100, default="Projekt_Nr", unique=False)
	
	def __str__(self):
		return self.NB_Ansprech
	def get_absolute_url(self):
		return reverse('certification82:netzbetreiberdetailview', kwargs={'pk': self.pk})	

#B
class Betreiber(models.Model):
	nameOK = models.BooleanField(default=False)
	name = models.CharField(max_length=250, default='No INFO')
	EZA_Betreiber_AnspreOK = models.BooleanField(default=False)
	EZA_Betreiber_Anspre = models.CharField(max_length=250, default=' ')
	# EZA_Betreiber_Name = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_StrNrOK = models.BooleanField(default=False)
	EZA_Betreiber_StrNr = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_PlzOrtOK = models.BooleanField(default=False)
	EZA_Betreiber_PlzOrt = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_TelOK = models.BooleanField(default=False)
	EZA_Betreiber_Tel = models.CharField(max_length=250, default=' ')
	EZA_Betreiber_MailOK = models.BooleanField(default=False)
	EZA_Betreiber_Mail = models.EmailField(max_length=70, blank=True, null=True, unique = True)
	Anlagenzert_NrOK = models.BooleanField(default=False)
	Anlagenzert_Nr = models.CharField(max_length=250, default=' ')

	EZA_Betreiber_AnspreTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Anspre", unique=False)
	EZA_Betreiber_NameTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Name", unique=False)
	EZA_Betreiber_StrNrTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_StrNr", unique=False)
	EZA_Betreiber_PlzOrtTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_PlzOrt", unique=False)
	EZA_Betreiber_TelTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Tel", unique=False)
	EZA_Betreiber_MailTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Mail", unique=False)
	Anlagenzert_NrTextmarke = models.CharField(max_length=100, default="Anlagenzert_Nr", unique=False)
	#so betr must have this field
	Projekt_NrOK = models.BooleanField(default=False)
	Projekt_Nr = models.BigIntegerField(default=0, unique=False)
	ProjekttitelOK = models.BooleanField(default=False)
	Projekttitel = models.CharField(max_length=250, default=' ')
	Projekt_NrTextmarke = models.CharField(max_length=100, default="Projekt_Nr", unique=False)
	ProjekttitelTextmarke = models.CharField(max_length=100, default="Projekttitel", unique=False)
	password1 = models.CharField(max_length=100 , default="f234dgthind2356")
	password2 = models.CharField(max_length=100, default="f234dgthind2356")
	login = models.CharField(max_length=100, unique=True, default="name123fdds44")
	# user = models.OneToOneField(User, on_delete = models.CASCADE, default="", null=True)
	projectuser = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE, default="", null=True)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('certification82:betreiberdetailview', kwargs={'pk': self.pk})	



#PM////////////////////////////////////////////////////
class ProjectManager(BaseUserManager):
	def create_user(self, projekt_nr, password=None):
		if not projekt_nr:
			raise ValueError('projekt_nr must be set!')
		user = self.model(projekt_nr=projekt_nr)
			# , first_name=first_name, last_name=last_name)
		user.set_password(password)
		user.is_stuff = True
		user.admin = False
		user.staff = False
		user.save(using=self._db)
		return user

	def create_superuser(self, projekt_nr, password):
		user = self.create_user(projekt_nr, password)
		user.is_admin = True
		user.admin = True
		user.staff = True
		user.is_stuff = True
		user.save(using=self._db)
		return user

	def natural_key(self, projekt_nr):
		return self.get(projekt_nr=projekt_nr)
#//////////////////////////////////////////////////////////////////////////////////
# class IsAdminUser(permissions.BasePermission):

# 	def has_permission(self, request, view):
# 		return request.user.is_admin
#PU
class ProjectUser(AbstractBaseUser):
	email = models.EmailField(max_length=255, unique=True, null = True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add = True)
	projekt_nr = models.BigIntegerField(default=10000001, unique = True)
	username= models.CharField(max_length=255, null=True)
	USERNAME_FIELD = 'projekt_nr'
	REQUIRED_FIELDS = []
	objects = ProjectManager()
	# permission_classes = (IsAdminUser,)
	def __str__(self):
		return str(self.projekt_nr)

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def get_full_name(self):
		return self.email

	def get_absolute_url(self):
		return reverse('certification82:projectuserdetailview', kwargs={'pk': self.pk})	


	@property
	def is_staff(self):
		return self._is_staff
	
	# @property
	# def _is_staff(self):
	# 	return self._is_staff

	@property
	def _is_admin(self):
		return self._is_admin
	
	@property
	def _is_active(self):
		return self._is_active
	


# class GetUserList(ListAPIView):
# 	permission_classes = (IsAdminUser,)
# 	queryset = Account.objects.all()
# 	serializer_class = AccountSerializer
# class BetreiberConnector(User):
# 	betreiber = models.OneToOneField(Betreiber, on_delete=models.CASCADE, primary_key=True,)


#Z
class Zertifikatsinhaber(models.Model):
	#project_id you will select zerfinh in project
	EZA_BezeichnungOK = models.BooleanField(default=False)
	EZA_Bezeichnung  = models.CharField(max_length=250, null=True)
	Zert_PartOK = models.BooleanField(default=False)
	Zert_Part = models.CharField(max_length=250, null=True)
	Zert_FirmOK = models.BooleanField(default=False)
	Zert_Firm = models.CharField(max_length=250, null=True)
	Zert_NrOK = models.BooleanField(default=False)
	Zert_Nr = models.CharField(max_length=250, null=True)
	Zert_PLZOK = models.BooleanField(default=False)
	Zert_PLZ = models.CharField(max_length=250, null=True)
	Zert_TelOK = models.BooleanField(default=False)
	Zert_Tel = models.CharField(max_length=250, null=True)
	Zert_FaxOK = models.BooleanField(default=False)
	Zert_Fax = models.CharField(max_length=250, null=True)
	Zert_MailOK = models.BooleanField(default=False)
	Zert_Mail = models.EmailField(max_length=70, blank=True, null=True, unique = True)

	EZA_BezeichnungTextmarke = models.CharField(max_length=100, default="EZA_BezeichnungTextmarke")
	Zert_PartTextmarke = models.CharField(max_length=100, default="Zert_Part")
	Zert_FirmTextmarke = models.CharField(max_length=100, default="Zert_Firm")
	Zert_NrTextmarke = models.CharField(max_length=100, default="Zert_Nr")
	Zert_PLZTextmarke = models.CharField(max_length=100, default="Zert_PLZ")
	Zert_TelTextmarke = models.CharField(max_length=100, default="Zert_Tel")
	Zert_FaxTextmarke = models.CharField(max_length=100, default="Zert_Fax")
	Zert_MailTextmarke = models.CharField(max_length=100, default="Zert_Mail")
	Projekt_Nr = models.BigIntegerField(default=0, unique=False)
	Projekt_NrOK=models.BooleanField(default=False)
	Projekt_NrTextmarke = models.CharField(max_length=100, default="Projekt_Nr", unique=False)
	def __str__(self):
		return self.EZA_Bezeichnung
	def get_absolute_url(self):
		return reverse('certification82:zertifikatsinhaberdetailview', kwargs={'pk': self.pk})	

#P
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
	#foreign keys
	netzbetreiber = models.ForeignKey(Netzbetreiber, on_delete=models.CASCADE, default="", null=True)
	betreiber = models.ForeignKey(Betreiber, on_delete=models.CASCADE, default="", null=True)
	zertifikatsinhaber = models.ForeignKey(Zertifikatsinhaber, on_delete=models.CASCADE, default="", null=True)
	
	EZA_Betreiber_AnspreTextmarke = models.CharField(max_length=100, default="EZA_Betreiber_Anspre")
	Zert_PartTextmarke = models.CharField(max_length=100, default="Zert_Part")

	Registriernummer_NB = models.BigIntegerField(default=0, unique=False, null=True)
	Registriernummer_NBTextmarke = models.CharField(max_length=250, default='Registriernummer_NB')
	def get_absolute_url(self):
		return reverse('certification82:projectdetailview', kwargs={'pk': self.id})

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.project_name
#E

class EzeHersteller(models.Model):
	hersteller_name = models.CharField(max_length=250, unique=True,null=False) 
	def __str__(self):
		return self.hersteller_name
	def get_absolute_url(self):
		return reverse('certification82:ezeherstellerdetailview', kwargs={'pk': self.id})

class EzeTyp(models.Model):
	typ_name = models.CharField(max_length=250, unique=True, null=False)	
	def __str__(self):
		return self.typ_name
	def get_absolute_url(self):
		return reverse('certification82:ezetypdetailview', kwargs={'pk': self.id})

class Eze(models.Model):
	#vDE_EZE1_Herst_id
	eZeHerstellerOK = models.BooleanField(default=False)
	eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE, default=None)
	#vDE_EZE1_Typ_id
	eZeTypOK = models.BooleanField(default=False)
	eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE, default=1)
	#every eze belongs to project
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	vDE_EZE1_NameOK = models.BooleanField(default=False)
	vDE_EZE1_Name = models.CharField(max_length=250)
	vDE_EZE1_ZertNROK = models.BooleanField(default=False)
	vDE_EZE1_ZertNR = models.BigIntegerField(default=0)	
	vDE_EZE1_SOK = models.BooleanField(default=False)
	vDE_EZE1_S = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_EZE1_POK = models.BooleanField(default=False)
	vDE_EZE1_P = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	vDE_Anzahl_EZE1OK = models.BooleanField(default=False)
	vDE_Anzahl_EZE1 = models.IntegerField(default=0)
	# eZeNeu_creation_date = models.DateField('date published', default='2019-01-01')
	VDE_EZE1_HerstTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Herst", unique=False)
	VDE_EZE1_TypTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Typ", unique=False)
	VDE_EZE1_NameTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Name", unique=False)
	VDE_EZE1_ZertNRTextmarke = models.CharField(max_length=100, default="VDE_EZE1_ZertNR", unique=False)
	VDE_EZE1_STextmarke = models.CharField(max_length=100, default="VDE_EZE1_S", unique=False)
	VDE_EZE1_PTextmarke = models.CharField(max_length=100, default="VDE_EZE1_P", unique=False)
	VDE_Anzahl_EZE1Textmarke = models.CharField(max_length=100, default="VDE_Anzahl_EZE1", unique=False)
	#for Generator
	VDE_EZE1_Motor = models.CharField(max_length=100, unique=False, null=True)
	VDE_EZE1_Generator = models.CharField(max_length=100, unique=False, null=True)
	VDE_EZE1_MotorOK = models.BooleanField(default=False)
	VDE_EZE1_GeneratorOK = models.BooleanField(default=False)
	VDE_EZE1_MotorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Motor", unique=False)
	VDE_EZE1_GeneratorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Generator", unique=False)


	ist_bestand = models.BooleanField(default=False)
	
	#if bestand....
	VDE_EZE_Bestand_Zahl = models.IntegerField(default=0, null=True)
	#vDE_EZE_Herst_Alt_id = //added EZE to Hersteller 13 12
	# EzeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE)
	#vDE_EZE_Typ_Alt_id 
	# EZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE)
	VDE_EZE_Name_ALT = models.CharField(max_length=250, null=True)
	VDE_S_EZE_Alt = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'), null=True)
	VDE_P_EZE_ALT = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000') , null=True)
	#jahr
	VDE_P_inbe_ALT = models.IntegerField(default=2019, null=True)

	VDE_EZE_Bestand_ZahlTextmarke = models.CharField(max_length=100,  default="VDE_EZE_Bestand_Zahl")
	#but we still need textmarks
	VDE_EZE_Herst_AltTextmarke = models.CharField(max_length=100, default="VDE_EZE_Herst_Alt" )
	VDE_EZE_Typ_AltTextmarke = models.CharField(max_length=100, default="VDE_EZE_Typ_Alt" )
	VDE_EZE_Name_ALTTextmarke = models.CharField(max_length=100, default="VDE_EZE_Name_ALT" )
	VDE_S_EZE_AltTextmarke = models.CharField(max_length=100, default="VDE_S_EZE_Alt" )
	VDE_P_EZE_ALTTextmarke = models.CharField(max_length=100, default="VDE_P_EZE_ALT" )
	VDE_P_inbe_ALTTextmarke = models.CharField(max_length=100, default="VDE_P_inbe_ALT" )
	VDE_EZE_Bestand_ZahlOK = models.BooleanField(default=False)
	#we do not need to double it. I want to optimize code. so.
	# EZeHerstellerOK = models.BooleanField(default=False)
	# EZeTypOK = models.BooleanField(default=False)
	
	VDE_EZE_Name_ALTOK = models.BooleanField(default=False)
	VDE_S_EZE_AltOK = models.BooleanField(default=False)
	VDE_P_EZE_ALTOK = models.BooleanField(default=False)
	VDE_P_inbe_ALTOK = models.BooleanField(default=False)

	def __str__(self):
		return self.vDE_EZE1_Name
	def get_absolute_url(self):
		return reverse('certification82:ezedetailview', kwargs={'pk': self.pk})

#T
class TrafoHersteller(models.Model):
	name = models.CharField(max_length=250, default='No INFO')
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('certification82:trafoherstellerdetailview', kwargs={'pk': self.id})

class TrafoTyp(models.Model):
	name = models.CharField(max_length=250, default='No INFO')
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('certification82:trafotypdetailview', kwargs={'pk': self.id})


class Transformator(models.Model):
	VDE_TrafoOK = models.BooleanField(default=False)
	VDE_Trafo = models.CharField(max_length=250, default='No INFO')
	VDE_TrafoherstellerOK = models.BooleanField(default=False)
	VDE_Trafohersteller = models.ForeignKey(TrafoHersteller, on_delete=models.CASCADE, default='No INFO')
	VDE_TrafotypOK = models.BooleanField(default=False)
	VDE_Trafotyp = models.ForeignKey(TrafoTyp, on_delete=models.CASCADE, default='No INFO')
	VDE_TrafoUeberOK = models.BooleanField(default=False)
	VDE_TrafoUeber = models.CharField(max_length=250, default='No INFO')
	VDE_TrafoOberOK = models.BooleanField(default=False)
	VDE_TrafoOber = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	VDE_TrafoUnterOK = models.BooleanField(default=False)
	VDE_TrafoUnter = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	VDE_Trafo_kurzOK = models.BooleanField(default=False)
	VDE_Trafo_kurz = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	VDE_Trafo_POK = models.BooleanField(default=False)
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
	def get_absolute_url(self):
		return reverse('certification82:transformatordetailview', kwargs={'pk': self.id})





















































######OLD
	##################################decomment after all created
class EzeNeu(models.Model):
	# vDE_EZE1_Herst_id
	# eZeHerstellerOK = models.BooleanField(default=False)
	# eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE, default=None)
	# #vDE_EZE1_Typ_id
	# eZeTypOK = models.BooleanField(default=False)
	# eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE, default=1)
	# #every eze belongs to project
	# project = models.ForeignKey(Project, on_delete=models.CASCADE)
	# vDE_EZE1_NameOK = models.BooleanField(default=False)
	# vDE_EZE1_Name = models.CharField(max_length=250)
	# vDE_EZE1_ZertNROK = models.BooleanField(default=False)
	# vDE_EZE1_ZertNR = models.BigIntegerField(default=0)	
	# vDE_EZE1_SOK = models.BooleanField(default=False)
	# vDE_EZE1_S = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	# vDE_EZE1_POK = models.BooleanField(default=False)
	# vDE_EZE1_P = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	# vDE_Anzahl_EZE1OK = models.BooleanField(default=False)
	# vDE_Anzahl_EZE1 = models.IntegerField(default=0)
	# #not for wind and foto
	# vDE_EZE1_MotorOK = models.BooleanField(default=False)
	# vDE_EZE1_Motor = models.CharField(max_length=250)
	# vDE_EZE1_GeneratorOK = models.BooleanField(default=False)
	# vDE_EZE1_Generator = models.CharField(max_length=250)
	# ##TEXTMARKEN
	# # eZeNeu_creation_date = models.DateField('date published', default='2019-01-01')
	# VDE_EZE1_HerstTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Herst")
	# VDE_EZE1_TypTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Typ")
	# VDE_EZE1_NameTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Name")
	# VDE_EZE1_ZertNRTextmarke = models.CharField(max_length=100, default="VDE_EZE1_ZertNR")
	# VDE_EZE1_MotorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Motor")
	# VDE_EZE1_GeneratorTextmarke = models.CharField(max_length=100, default="VDE_EZE1_Generator")
	# VDE_EZE1_STextmarke = models.CharField(max_length=100, default="VDE_EZE1_S")
	# VDE_EZE1_PTextmarke = models.CharField(max_length=100, default="VDE_EZE1_P")
	# VDE_Anzahl_EZE1Textmarke = models.CharField(max_length=100, default="VDE_Anzahl_EZE1")
	
	def __str__(self):
		return self.vDE_EZE1_Name

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class EzeBestand(models.Model):
	#every ezebestand belongs to a specific Project
	# project = models.ForeignKey(Project, on_delete=models.CASCADE)

	# vDE_EZE_Bestand_Zahl = models.IntegerField(default=0)
	# #vDE_EZE_Herst_Alt_id = //added EZE to Hersteller 13 12
	# eZeHersteller = models.ForeignKey(EzeHersteller, on_delete=models.CASCADE)
	# #vDE_EZE_Typ_Alt_id 
	# eZeTyp = models.ForeignKey(EzeTyp, on_delete=models.CASCADE)
	# vDE_EZE_Name_ALT = models.CharField(max_length=250)
	# vDE_S_EZE_Alt = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	# vDE_P_EZE_ALT = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
	# #jahr
	# vDE_P_inbe_ALT = models.IntegerField(default=0)

	# VDE_EZE_Bestand_ZahlTextmarke = models.CharField(max_length=100,  default="VDE_EZE_Bestand_Zahl")
	# VDE_EZE_Herst_AltTextmarke = models.CharField(max_length=100, default="VDE_EZE_Herst_Alt" )
	# VDE_EZE_Typ_AltTextmarke = models.CharField(max_length=100, default="VDE_EZE_Typ_Alt" )
	# VDE_EZE_Name_ALTTextmarke = models.CharField(max_length=100, default="VDE_EZE_Name_ALT" )
	# VDE_S_EZE_AltTextmarke = models.CharField(max_length=100, default="VDE_S_EZE_Alt" )
	# VDE_P_EZE_ALTTextmarke = models.CharField(max_length=100, default="VDE_P_EZE_ALT" )
	# VDE_P_inbe_ALTTextmarke = models.CharField(max_length=100, default="VDE_P_inbe_ALT" )

	def __str__(self):
		return self.vDE_EZE_Name_ALT

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

