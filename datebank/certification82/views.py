#rendering possible
from django.shortcuts import get_object_or_404, render, redirect
#add 404
from django.http import Http404
###or HttpResponseRedirect
from django.http import HttpResponse
#lazy reverse
from django.urls import reverse_lazy
from .models import EzeNeu, EzeBestand, Project, EzeBestGenerator, \
EzeBestFotovoltaic, EzeBestWindkraft, Eze, EzeNeuGenerator, EzeNeuWindkraft,\
 EzeNeuFotovoltaic, Document, TrafoTyp, Transformator, Betreiber, User, Zertifikatsinhaber, Netzbetreiber#, Schutz, Regelung
from django.template import loader
#add pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth import login, authenticate
from .forms import BetreiberForm, NetzBetreiberForm,\
 ZertifikatsinhaberForm, ProjectForm,\
 NewEzeNeuForm, NewEzeBestForm, NewHerstellerForm, NewEzeTypForm
	
# Create your views here.
# def index(request):
# 	project_name_list = Project.objects.order_by('-project_creation_date')[:3]
# 	latest_EzeNeu_list = EzeNeu.objects.order_by('-vDE_EZE1_Name')[:3]
# 	eze_Neus = ', '.join([e.vDE_EZE1_Name for e in latest_EzeNeu_list])
# 	# project_Names = ' , '.join([p.project_name for p in project_name])
# 	#added template
# 	template = loader.get_template('certification82/index.html')
# 	context = {	'project_name_list': project_name_list, }
# 	return render(request, 'certification82/index.html', context)
	# return HttpResponse(project_Names+'\n\n<br> Neue Ezes: \n'+eze_Neus )
#add more views
####USing GENERIC add at the top from django.views import generic from django.urls import reverse

#//////101019///////////////////////////////////////////////////////////
def new_eze_typ(request):
	if request.method == 'POST':
		form = NewEzeTypForm(request.POST)
		if form.is_valid():
			form.save()
			typ_name = form.cleaned_data.get("typ_name")

			ezetyp = form.save()
			print ('\n\nnew EzeTyp created\n\n')
			return redirect('certification82:new_eze_neu')
	else:
		form = NewEzeTypForm()
	return render(request, 'new/ezetyp.html',{'form':form})
#//////////////////////////////////////////////////////////////////
#//////////////////10/10/19/////////added/////////////////////////
def new_hersteller(request):
	if request.method == 'POST':
		form = NewHerstellerForm(request.POST)
		if form.is_valid():
			form.save()
			hersteller_name = form.cleaned_data.get("hersteller_name")

			ezehersteller = form.save()
			print ('\n\nnew Hersteller created\n\n')
			return redirect('certification82:new_eze_neu')
	else:
		form = NewHerstellerForm()
	return render(request, 'new/hersteller.html',{'form':form})
#//////////////////////////////////////////////////////////////////

#NEN
def new_eze_neu(request):
	if request.method == 'POST':
		form = NewEzeNeuForm(request.POST)
		if form.is_valid():
			form.save()
			Zert_MailTextmarke = form.cleaned_data.get("Zert_Mail")

			eze = form.save()
			print ('\n\nnew EZE neu created\n\n')
			return redirect('certification82:index')
	else:
		form = NewEzeNeuForm()
	return render(request, 'new/eze.html',{'form':form})
#NEB
def new_eze_bestand(request):
	if request.method == 'POST':
		form = NewEzeBestForm(request.POST)
		if form.is_valid():
			form.save()
			Zert_MailTextmarke = form.cleaned_data.get("Zert_Mail")

			eze = form.save()
			print ('\n\nnew Eze Bestand created\n\n')
			return redirect('certification82:index')
	else:
		form = NewEzeBestForm()
	return render(request, 'new/eze.html',{'form':form})

#NP
def new_projekt(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			project_name = form.cleaned_data.get('project_name')
			project_number  = form.cleaned_data.get('project_number')
			project_deadline_date = form.cleaned_data.get('project_deadline_date')
			is_done = form.cleaned_data.get('is_done')
			access_for_user = form.cleaned_data.get('access_for_user')
			access_for_moderator = form.cleaned_data.get('access_for_moderator')
			access_for_admin = form.cleaned_data.get('access_for_admin')
			Projekt_NrTexmarke = form.cleaned_data.get('Projekt_NrTexmarke')
			ProjekttitelTexmarke = form.cleaned_data.get('ProjekttitelTexmarke')
			Projekt_DateTexmarke = form.cleaned_data.get('Projekt_DateTexmarke')
			Anlagenzert_NrTexmarke = form.cleaned_data.get('Anlagenzert_NrTexmarke')
			netzbetreiberTextmarke = form.cleaned_data.get('netzbetreiberTextmarke')
			betreiberTextmarke = form.cleaned_data.get('betreiberTextmarke')
			netzbetreiber =form.cleaned_data.get('netzbetreiber')
			betreiber = form.cleaned_data.get('betreiber')
			zertifikatsinhaber = form.cleaned_data.get('zertifikatsinhaber')

			EZA_Betreiber_AnspreTextmarke = form.cleaned_data.get("EZA_Betreiber_AnspreTextmarke")
			Zert_PartTextmarke = form.cleaned_data.get("Zert_PartTextmarke")
			Registriernummer_NB = form.cleaned_data.get("Registriernummer_NB")
			Registriernummer_NBTextmarke = form.cleaned_data.get("Registriernummer_NBTextmarke")
			
			project = form.save()
			print ('\n\nnew Project created\n\n')
			# login(request, user)
			return redirect('certification82:index')
	else:
		# project = get_object_or_404(Project, id=project_number)
		form = ProjectForm()
	# return render(request, 'registration/signup.html', {'form': form})

	# form = BetreiberForm()
	return render(request, 'new/projekt.html',{'form':form})
#NZ
def new_zert(request):
	if request.method == 'POST':
		form = ZertifikatsinhaberForm(request.POST)
		if form.is_valid():
			form.save()
			EZA_BezeichnungOK = form.cleaned_data.get('EZA_BezeichnungOK')
			EZA_Bezeichnung  = form.cleaned_data.get('EZA_Bezeichnung')
			Zert_PartOK = form.cleaned_data.get('Zert_PartOK')
			Zert_Part = form.cleaned_data.get('Zert_Part')
			Zert_FirmOK = form.cleaned_data.get('Zert_FirmOK')
			Zert_Firm = form.cleaned_data.get('Zert_Firm')
			Zert_NrOK = form.cleaned_data.get('Zert_NrOK')
			Zert_Nr = form.cleaned_data.get('Zert_Nr')
			Zert_PLZOK = form.cleaned_data.get('Zert_PLZOK')
			Zert_PLZ = form.cleaned_data.get('Zert_PLZ')
			Zert_TelOK = form.cleaned_data.get('Zert_TelOK')
			Zert_Tel = form.cleaned_data.get('Zert_Tel')
			Zert_FaxOK = form.cleaned_data.get('Zert_FaxOK')
			Zert_Fax =form.cleaned_data.get('Zert_Fax')
			Zert_MailOK = form.cleaned_data.get('Zert_MailOK')
			Zert_Mail = form.cleaned_data.get('Zert_Mail')

			EZA_BezeichnungTextmarke = form.cleaned_data.get("EZA_BezeichnungTextmarke")
			Zert_PartTextmarke = form.cleaned_data.get("Zert_Part")
			Zert_FirmTextmarke = form.cleaned_data.get("Zert_Firm")
			Zert_NrTextmarke = form.cleaned_data.get("Zert_Nr")
			Zert_PLZTextmarke = form.cleaned_data.get("Zert_PLZ")
			Zert_TelTextmarke = form.cleaned_data.get("Zert_Tel")
			Zert_FaxTextmarke = form.cleaned_data.get("Zert_Fax")
			Zert_MailTextmarke = form.cleaned_data.get("Zert_Mail")

			zertifikatsinhaber = form.save()
			print ('\n\nnew Zertifikatsinhaber created\n\n')
			# login(request, user)
			return redirect('certification82:index')
	else:
		form = ZertifikatsinhaberForm()
	# return render(request, 'registration/signup.html', {'form': form})

	# form = BetreiberForm()
	return render(request, 'new/zertifikatsinhaber.html',{'form':form})
#NN
def new_netzbetreiber(request):
	if request.method == 'POST':
		form = NetzBetreiberForm(request.POST)
		if form.is_valid():
			form.save()
			NB_AnsprechOK = form.cleaned_data.get('nameOK')
			NB_Ansprech = form.cleaned_data.get('NB_Ansprech')
			NB_NameOK = form.cleaned_data.get('NB_NameOK')
			NB_Name = form.cleaned_data.get('NB_Name')
			NB_StrOK = form.cleaned_data.get('NB_StrOK')
			NB_Str = form.cleaned_data.get('NB_Str')
			NB_PLZOK = form.cleaned_data.get('NB_PLZOK')
			NB_PLZ = form.cleaned_data.get('NB_PLZ')
			NB_TelOK = form.cleaned_data.get('NB_TelOK')
			NB_Tel = form.cleaned_data.get('NB_Tel')
			NB_FaxOK = form.cleaned_data.get('NB_FaxOK')
			NB_Fax = form.cleaned_data.get('NB_Fax')
			NB_MailOK = form.cleaned_data.get('NB_MailOK')
			NB_Mail = form.cleaned_data.get('NB_Mail')
			NB_AnsprechTextmarke = form.cleaned_data.get('NB_AnsprechTextmarke')
			NB_NameTextmarke = form.cleaned_data.get('NB_NameTextmarke')
			NB_StrTextmarke = form.cleaned_data.get('NB_StrTextmarke')
			NB_PLZTextmarke = form.cleaned_data.get('NB_PLZTextmarke')
			NB_TelTextmarke = form.cleaned_data.get('NB_TelTextmarke')
			NB_FaxTextmarke = form.cleaned_data.get('NB_FaxTextmarke')
			NB_MailTextmarke = form.cleaned_data.get('NB_MailTextmarke')

			netzbetreiber = form.save()
			print ('new NETZbetreiber created')
			# login(request, user)
			return redirect('certification82:index')
	else:
		form = NetzBetreiberForm()
	# return render(request, 'registration/signup.html', {'form': form})

	# form = BetreiberForm()
	return render(request, 'new/netzbetreiber.html',{'form':form})

#NB
def new_betreiber(request):
	if request.method == 'POST':
		form = BetreiberForm(request.POST)
		if form.is_valid():
			form.save()
			nameOK = form.cleaned_data.get('nameOK')
			name = form.cleaned_data.get('name')
			EZA_Betreiber_AnspreOK = form.cleaned_data.get('EZA_Betreiber_AnspreOK')
			EZA_Betreiber_Anspre = form.cleaned_data.get('EZA_Betreiber_Anspre')
			EZA_Betreiber_StrNrOK = form.cleaned_data.get('EZA_Betreiber_StrNrOK')
			EZA_Betreiber_StrNr = form.cleaned_data.get('EZA_Betreiber_StrNr')
			EZA_Betreiber_PlzOrtOK = form.cleaned_data.get('EZA_Betreiber_PlzOrtOK')
			EZA_Betreiber_PlzOrt = form.cleaned_data.get('EZA_Betreiber_PlzOrt')
			EZA_Betreiber_TelOK = form.cleaned_data.get('EZA_Betreiber_TelOK')
			EZA_Betreiber_Tel = form.cleaned_data.get('EZA_Betreiber_Tel')
			EZA_Betreiber_MailOK = form.cleaned_data.get('EZA_Betreiber_MailOK')
			EZA_Betreiber_Mail = form.cleaned_data.get('EZA_Betreiber_Mail')
			Anlagenzert_NrOK = form.cleaned_data.get('Anlagenzert_NrOK')
			Anlagenzert_Nr = form.cleaned_data.get('Anlagenzert_Nr')
			Projekt_NrOK = form.cleaned_data.get('Projekt_NrOK')
			Projekt_Nr = form.cleaned_data.get('Projekt_Nr')
			ProjekttitelOK = form.cleaned_data.get('ProjekttitelOK')
			Projekttitel = form.cleaned_data.get('Projekttitel')

			# projekt_nr = form.cleaned_data.get('projekt_nr')
			# raw_password = form.cleaned_data.get('password1')
			# email = form.cleaned_data.get('EZA_Betreiber_Mail')
			# first_last_name = form.cleaned_data.get('first_name')
			betreiber = form.save()
			print ('new betreiber created')
			# login(request, user)
			return redirect('certification82:index')
	else:
		form = BetreiberForm()
	# return render(request, 'registration/signup.html', {'form': form})

	# form = BetreiberForm()
	return render(request, 'new/betreiber.html',{'form':form})
#A
def allgeminfo(request, projekt_nr):
	project = Project.objects.filter(project_number=projekt_nr)
	# print(project)
	# for proj in project:
	# 	print(proj.id)
	# 	print(proj.project_number)
		

	# print(project.objects.all())
	# items = EzeNeuGenerator.objects.filter(project_id=project_id)
	# context = {'project' : project, 'items':items }
	# return render(request, 'certification82/ezeneugenofproindex.html', context)
	# ezen = get_object_or_404(Project, pk = project_id)
	betreiber = Betreiber.objects.filter(Projekt_Nr=projekt_nr)
	if not betreiber:
		print('no betr added ')
		print('proofing....')
		print(Betreiber.objects.all)

	print(betreiber)
	for proj in betreiber:
		print('we are in cycle betreiber')
		print(proj.Projekt_Nr)
		print(proj.projectuser)
	
	zertifikatsinhaber = Zertifikatsinhaber.objects.filter(Projekt_Nr=projekt_nr)
	print(zertifikatsinhaber)
	print('zert is...')
	a=Zertifikatsinhaber.objects.all()
	print(a[1].Projekt_Nr)
	netzbetreiber = Netzbetreiber.objects.filter(Projekt_Nr=projekt_nr)
	print(netzbetreiber)
	ezebestand = Eze.objects.filter(project=projekt_nr, ist_bestand=True)
	ezeneu = Eze.objects.filter(project=projekt_nr, ist_bestand=False)
	context={'ezebestand':ezebestand,'ezeneu':ezeneu,'betreiber' : betreiber, 'project' : project}

	# ezebestwindkraft = EzeBestWindkraft.objects.filter(project=projekt_nr)
	# ezeneuwind = EzeNeuWindkraft.objects.filter(project=projekt_nr)
	# ezeneufotovoltaic = EzeNeuFotovoltaic.objects.filter(project=projekt_nr)
	# ezebestfotovoltaic = EzeBestFotovoltaic.objects.filter(project=projekt_nr)
	# ezeneugen = EzeNeuGenerator.objects.filter(project=projekt_nr)
	# ezebestgenerator = EzeBestGenerator.objects.filter(project=projekt_nr)
	# context = {'betreiber' : betreiber, 'project' : project, \
	# 'ezeneuwind': ezeneuwind, 'ezeneugen': ezeneugen,\
	# 'zertifikatsinhaber':zertifikatsinhaber,'netzbetreiber':netzbetreiber,\
	# 'ezeneufotovoltaic':ezeneufotovoltaic, 'ezebestwindkraft': ezebestwindkraft,\
	#    'ezebestfotovoltaic': ezebestfotovoltaic, 'ezebestgenerator':ezebestgenerator }
	
	return render(request, 'certification82/allgeminfo.html', context)
#E
class EzeCreate(CreateView):
	model = Eze
class EzeUpdate(UpdateView):
	model = Eze
	fields = [
	\
			'eZeHersteller','eZeHerstellerOK','VDE_EZE1_HerstTextmarke',\
			'eZeTyp','eZeTypOK','VDE_EZE1_TypTextmarke','project',\
			'vDE_EZE1_Name','vDE_EZE1_NameOK','VDE_EZE1_NameTextmarke',\
			'vDE_EZE1_ZertNR','vDE_EZE1_ZertNROK','VDE_EZE1_ZertNRTextmarke',\
			'vDE_EZE1_S','vDE_EZE1_SOK','VDE_EZE1_STextmarke',\
			'vDE_EZE1_P','vDE_EZE1_POK','VDE_EZE1_PTextmarke',\
			'vDE_Anzahl_EZE1','vDE_Anzahl_EZE1OK','VDE_Anzahl_EZE1Textmarke',\
			'VDE_EZE1_Motor','VDE_EZE1_MotorOK','VDE_EZE1_MotorTextmarke',\
			'VDE_EZE1_Generator','VDE_EZE1_GeneratorOK','VDE_EZE1_GeneratorTextmarke',\
			'ist_bestand'
	]
	template_name_suffix = '_update_form'
class EzeDelete(DeleteView):
	model = Eze
	success_url = reverse_lazy('certification82:index')

class EzeDetailView(generic.DetailView):
	model = Eze
	template_name = 'certification82/detailed_views/eze_detail.html'

#P
class ProjectCreate(CreateView):
	model = Project
	fields = [
	'project_name','project_number','project_deadline_date','is_done','access_for_user',
	'access_for_moderator','access_for_admin','Projekt_NrTexmarke','ProjekttitelTexmarke','Projekt_DateTexmarke',
	'Anlagenzert_NrTexmarke','netzbetreiberTextmarke','betreiberTextmarke','netzbetreiber','betreiber',
	'zertifikatsinhaber','EZA_Betreiber_AnspreTextmarke','Zert_PartTextmarke','Registriernummer_NB','Registriernummer_NBTextmarke']
class ProjectUpdate(UpdateView):
	model = Project
	fields = [
	'project_name','project_number','project_deadline_date','is_done','access_for_user',
	'access_for_moderator','access_for_admin','Projekt_NrTexmarke','ProjekttitelTexmarke','Projekt_DateTexmarke',
	'Anlagenzert_NrTexmarke','netzbetreiberTextmarke','betreiberTextmarke','netzbetreiber','betreiber',
	'zertifikatsinhaber','EZA_Betreiber_AnspreTextmarke','Zert_PartTextmarke','Registriernummer_NB','Registriernummer_NBTextmarke']

	template_name_suffix = '_form'
class ProjectDelete(DeleteView):
	model = Project
	success_url = reverse_lazy('certification82:index')
	#delete is working tessted 11 10 19
class ProjectDetailView(generic.DetailView):
	model = Project
	template_name = 'certification82/detailed_views/project_detail.html'

class ProjectView(generic.ListView):
	template_name = 'certification82/index.html'
	context_object_name = 'project_name_list'

	def get_queryset(self):
		# user = get_object_or_404(User, pk=id)
		"""Return the last five published questions."""
		# return Project.objects.filter(project_number==user.projekt_Nr)[:5]

		# user= get_object_or_404(Betreiber, betreiber_id=pk)
		# return Project.objects.filter(project_number=user.projekt_nr)[:5]
		return Project.objects.order_by('-project_number')[:5]

#I
class IndexView(generic.ListView):
	template_name = 'certification82/index.html'
	context_object_name = 'project_name_list'

	def get_queryset(self):
		# user = get_object_or_404(User, pk=id)
		"""Return the last five published questions."""
		# return Project.objects.filter(project_number==user.projekt_Nr)[:5]

		# user= get_object_or_404(Betreiber, betreiber_id=pk)
		# return Project.objects.filter(project_number=user.projekt_nr)[:5]
		return Project.objects.order_by('-project_number')[:5]
#####new and best gener views of index
#neuwind
class NeuWindkraftIndexView(generic.ListView):
	#or modelname_list.html
	template_name = 'certification82/list_views/EzeNeuWindkraft_list.html'
	context_object_name = 'neuwindkraft_name_list'
	def get_queryset(self):
		return EzeNeuWindkraft.objects.order_by('-name')[:5]
class NeuWindkraftDetailView(generic.DetailView):
	model = EzeNeuWindkraft
	template_name = 'certification82/detailed_views/EzeNeuWindkraft_detail.html' #or ModelName_detail.html
#bestwind
class BestWindkraftIndexView(generic.ListView):
	context_object_name = 'bestwindkraft_name_list'
	template_name = 'certification82/list_views/EzeBestWindkraft_list.html'
	def get_queryset(self):
		return EzeBestWindkraft.objects.order_by('-name')[:5]
class BestWindkraftDetailView(generic.DetailView):
	model = EzeBestWindkraft
	template_name = 'certification82/detailed_views/EzeBestWindkraft_detail.html' #or ModelName_detail.html
#neufoto
class NeuFotovoltaicIndexView(generic.ListView):
	context_object_name = 'neufotovoltaic_name_list'
	template_name = 'certification82/list_views/EzeNeuFotovoltaic_list.html'

	def get_queryset(self):
		return EzeNeuFotovoltaic.objects.order_by('-name')[:5]
class NeuFotovoltaicDetailView(generic.DetailView):
	model = EzeNeuFotovoltaic
	template_name = 'certification82/detailed_views/EzeNeuFotovoltaic_detail.html'
#bestfoto
class BestFotovoltaicIndexView(generic.ListView):
	context_object_name = 'bestfotovoltaic_name_list'
	template_name = 'certification82/list_views/EzeBestFotovoltaic_list.html'
	def get_queryset(self):
		return EzeBestFotovoltaic.objects.order_by('-name')[:5]
class BestFotovoltaicDetailView(generic.DetailView):
	model = EzeBestFotovoltaic
	template_name = 'certification82/detailed_views/EzeBestFotovoltaic_detail.html'
#neugen
class NeuGeneratorIndexView(generic.ListView):
	context_object_name = 'neugen_name_list'
	template_name = 'certification82/list_views/EzeNeuGenerator_list.html'
	def get_queryset(self):
		"""Return the last a-z added generators."""
		return EzeNeuGenerator.objects.order_by('-name')[:5]
class NeuGeneratorDetailView(generic.DetailView):
	model = EzeNeuGenerator
	template_name = 'certification82/detailed_views/EzeNeuGenerator_detail.html'


class BestGeneratorIndexView(generic.ListView):
	context_object_name = 'bestgen_name_list'
	template_name = 'certification82/list_views/EzeBestGenerator_list.html'
	def get_queryset(self):
		return EzeBestGenerator.objects.order_by('-name')[:5]
class BestGeneratorDetailView(generic.DetailView):
	model = EzeBestGenerator
	template_name = 'certification82/detailed_views/EzeBestGenerator_detail.html'



# class EveryProjectDetailView(generic.DetailView):
# 	model = Project
# 	template_name = 'certification82/detail.html'

	# def get_object(context, project_id):
		# try:OLD
		# project_id = self.get_object().id
		# ezen = get_object_or_404(Project, pk = project_id)
		# ezeneuwind = EzeNeuWindkraft.objects.filter(project_id=project_id)
		# ezeneugen = EzeNeuGenerator.objects.filter(project_id=project_id)
		# ezeneufotovoltaic = EzeNeuFotovoltaic.objects.filter(project_id=project_id)
		# ezebestwindkraft = EzeBestWindkraft.objects.filter(project_id=project_id)
		# ezebestfotovoltaic = EzeBestFotovoltaic.objects.filter(project_id=project_id)
		# ezebestgenerator = EzeBestGenerator.objects.filter(project_id=project_id)
		# # .filter(project_id=project_id)
		# context = {'ezen':ezen, 'ezeneuwind': ezeneuwind, 'ezeneugen': ezeneugen, 'ezeneufotovoltaic':ezeneufotovoltaic, 'ezebestwindkraft': ezebestwindkraft, 'ezebestfotovoltaic': ezebestfotovoltaic, 'ezebestgenerator':ezebestgenerator }
	
		# # return get_object_or_404(Project, pk=request.session['user_id'])
		# return render(request, 'certification82/detail.html', context)

#########################################################################
#new

# def documenteindex(request):
# 	alldocuments = Document.objects.all()
# 	context = {'alldocuments' : alldocuments }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)
class DocumentIndexView(generic.ListView):
	context_object_name = 'document_name_list'
	template_name = 'certification82/list_views/Document_list.html'
	def get_queryset(self):
		return Document.objects.order_by('-name')[:5]
class DocumentDetailView(generic.DetailView):
	model = Document
	template_name = 'certification82/detailed_views/Document_detail.html'

class DocumentCreate(CreateView):
	model = Document
class DocumentUpdate(UpdateView):
	model = Document
class DocumentDelete(DeleteView):
	model = Document



# def betreiberindex(request):
# 	allbetreibers = Betreiber.objects.all()
# 	context = {'allbetreibers' : allbetreibers }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)
class BetreiberIndexView(generic.ListView):
	context_object_name = 'betreiber_name_list'
	template_name = 'certification82/list_views/Betreiber_list.html'
	def get_queryset(self):
		return Betreiber.objects.order_by('-name')[:5]
class BetreiberDetailView(generic.DetailView):
	model = Betreiber
	template_name = 'certification82/detailed_views/Betreiber_detail.html'

class BetreiberCreate(CreateView):
	model = Betreiber
class BetreiberUpdate(UpdateView):
	model = Betreiber
class BetreiberDelete(DeleteView):
	model = Betreiber


def schutzindex(request):
	allschutz = Schutz.objects.all()
	context = {'allschutz' : allschutz }
	#CHANGE IT!
	return render(request, 'certification82/ezeneuwindindex.html', context)

# def trafoindex(request):
# 	alltransformators = Transformator.objects.all()
# 	context = {'alltransformators' : alltransformators }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)

#!TRANSFORMATOR!
class TransformatorIndexView(generic.ListView):
	context_object_name = 'transformator_name_list'
	template_name = 'certification82/list_views/Transformator_list.html'
	def get_queryset(self):
		return Transformator.objects.order_by('-VDE_Trafo')[:5]
class TransformatorDetailView(generic.DetailView):
	model = Transformator
	template_name = 'certification82/detailed_views/Transformator_detail.html'
class TransformatorCreate(CreateView):
	model = Transformator
class TransformatorUpdate(UpdateView):
	model = Transformator
class TransformatorDelete(DeleteView):
	model = Transformator

def regelungindex(request):
	allregelungs = Regelung.objects.all()
	context = {'allregelungs' : allregelungs }
	#CHANGE IT!
	return render(request, 'certification82/ezeneuwindindex.html', context)



#good
def ezeneuwindindex(request):
	ezeneuwind = EzeNeuWindkraft.objects.all()
	# ezeneuwind = get_object_or_404(EzeNeuWindkraft, pk = ezeneuwindkraft_id)
	context = {'ezeneuwind' : ezeneuwind }
	return render(request, 'certification82/ezeneuwindindex.html', context)
#???
def ezeneuwindkraftsoftheprojectindex(request, project_number):
	ezeneuwindofpro = get_object_or_404(Project, pk = project_number)
	ezeneuwind = EzeNeuWindkraft.objects.filter(project=project_number)
	
	# ezeneuwind = get_object_or_404(EzeNeuWindkraft, pk = ezeneuwindkraft_id)
	context = {'ezeneuwindofpro' : ezeneuwindofpro, 'ezeneuwind':ezeneuwind }
	return render(request, 'certification82/ezeneuwindofproindex.html', context)
#indexes of that
def ezeneufotooftheprojectindex(request, project_id):
	project = get_object_or_404(Project, pk = project_id)
	items = EzeNeuFotovoltaic.objects.filter(project_id=project_id)
	context = {'project' : project, 'items':items }
	return render(request, 'certification82/ezeneufotoofproindex.html', context)
def ezeneugenoftheprojectindex(request, project_id):
	project = get_object_or_404(Project, pk = project_id)
	items = EzeNeuGenerator.objects.filter(project_id=project_id)
	context = {'project' : project, 'items':items }
	return render(request, 'certification82/ezeneugenofproindex.html', context)

def ezebestwindoftheprojectindex(request, project_id):
	project = get_object_or_404(Project, pk = project_id)
	items = EzeBestWindkraft.objects.filter(project_id=project_id)
	context = {'project' : project, 'items':items }
	return render(request, 'certification82/ezebestwindofproindex.html', context)
def ezebestfotooftheprojectindex(request, project_id):
	project = get_object_or_404(Project, pk = project_id)
	items = EzeBestFotovoltaic.objects.filter(project_id=project_id)
	context = {'project' : project, 'items':items }
	return render(request, 'certification82/ezebestfotoofproindex.html', context)
def ezebestgenoftheprojectindex(request, project_id):
	project = get_object_or_404(Project, pk = project_id)
	items = EzeBestGenerator.objects.filter(project_id=project_id)
	context = {'project' : project, 'items':items }
	return render(request, 'certification82/ezebestgenofproindex.html', context)





################################################################################################3

def detail(request, project_id):
	# try:
	ezen = get_object_or_404(Project, pk = project_id)
	eze = Eze.objects.filter(project_id=project_id)
	context = { 'ezen':ezen, 'eze':eze }
	# ezeneuwind = EzeNeuWindkraft.objects.filter(project_id=project_id)
	# ezeneugen = EzeNeuGenerator.objects.filter(project_id=project_id)
	# ezeneufotovoltaic = EzeNeuFotovoltaic.objects.filter(project_id=project_id)
	# ezebestwindkraft = EzeBestWindkraft.objects.filter(project_id=project_id)
	# ezebestfotovoltaic = EzeBestFotovoltaic.objects.filter(project_id=project_id)
	# ezebestgenerator = EzeBestGenerator.objects.filter(project_id=project_id)
	# allneuezes = {'ezeneuwind': ezeneuwind, 'ezeneugen': ezeneugen, 'ezeneufotovoltaic':ezeneufotovoltaic}
	# allbestezes = {'ezebestwindkraft': ezebestwindkraft, 'ezebestgenerator':ezebestgenerator, 'ezebestfotovoltaic': ezebestfotovoltaic}
	# # .filter(project_id=project_id)
	# context = {'allneuezes' : allneuezes, 'allbestezes' : allbestezes, 'ezen' : ezen, 'ezeneuwind': ezeneuwind, 'ezeneugen': ezeneugen, 'ezeneufotovoltaic':ezeneufotovoltaic, 'ezebestwindkraft': ezebestwindkraft, 'ezebestfotovoltaic': ezebestfotovoltaic, 'ezebestgenerator':ezebestgenerator }
	# eze_neu_list = EzeNeu.objects.all()
	# eze_best_list = EzeBestand.objects.all()
	# eze_neu_wind_list = EzeNeuWindkraft.objects.all()
	

	# page = request.GET.get('page', 1)
	# #paginator1
	# paginator = Paginator(eze_neu_list, 2)
	# try:
	# 	ezes = paginator.page(page)
	# except PageNotAnInteger:
	# 	ezes = paginator.page(1)
	# except EmptyPage:
	# 	ezes = paginator.page(paginator.num_pages)

	# except EzeNeu.DoesNotExist:
	# raise Http404("No Eze with this project number: "+str(project_id))
	# context = {	'latest_EzeNeu_list': latest_EzeNeu_list, }
	
	return render(request, 'certification82/detail.html', context)

#shows only 1 result exactly with number given by link

def project_show(request, project_id):
	pro1 = get_object_or_404(Project, pk = project_id)
	project_list = Project.objects.all()
	ezeneuwind = EzeNeuWindkraft.objects.filter(project_id=project_id)
	ezeneugen = EzeNeuGenerator.objects.filter(project_id=project_id)
	ezeneufotovoltaic = EzeNeuFotovoltaic.objects.filter(project_id=project_id)
	ezebestwindkraft = EzeBestWindkraft.objects.filter(project_id=project_id)
	ezebestfotovoltaic = EzeBestFotovoltaic.objects.filter(project_id=project_id)
	ezebestgenerator = EzeBestGenerator.objects.filter(project_id=project_id)
	context = {'pro1' :pro1, 'ezeneuwind': ezeneuwind, 'ezeneugen': ezeneugen, 'ezeneufotovoltaic':ezeneufotovoltaic, 'ezebestwindkraft': ezebestwindkraft, 'ezebestfotovoltaic': ezebestfotovoltaic, 'ezebestgenerator':ezebestgenerator }
	return render(request, 'certification82/project_show.html', context)

def eze_neu_show(request, ezeneu_id):
	ezeneu1 = get_object_or_404(Eze, pk = id)
	eze_neu_list = Eze.objects.all()	
	return render(request, 'certification82/eze_neu_show.html', {'ezeneu1' :ezeneu1 })

def eze_best_show(request, ezeneu_id):
	ezeneu1 = get_object_or_404(EzeBestand, pk = ezebestand_id)
	eze_best_list = EzeBestand.objects.all()
	
	return render(request, 'certification82/eze_best_show.html', {'ezeneu1' :ezeneu1 })

def results(request, project_id):
	response = "You're looking at the results of project %s."
	return HttpResponse(response % project_id)

def vote(request, project_id):
	return HttpResponse("You're voting on project %s." % project_id)

def ezenues(request):
	# project_name = Project.objects.order_by('-project_name')[:3]
	latest_EzeNeu_list = EzeNeu.objects.order_by('-vDE_EZE1_Name')[:3]
	eze_Neus = ', '.join([e.vDE_EZE1_Name for e in latest_EzeNeu_list])
	# project_Names = ', '.join([p.project_name for p in project_name])
	return HttpResponse('<br> <h2>Neue Ezes:</h2> <br>'+eze_Neus )

def ezebestands(request):
	# project_name = Project.objects.order_by('-project_name')[:3]
	latest_EzeBestand_list = EzeBestand.objects.order_by('-vDE_EZE_Name_ALT')[:3]
	eze_Bestands = ', '.join([e.vDE_EZE_Name_ALT for e in latest_EzeBestand_list])
	# project_Names = ', '.join([p.project_name for p in project_name])
	return HttpResponse('\n\n<br> Ezes Bestand: \n'+eze_Bestands )




#####OLD



# def ezebestwindindex(request):
# 	allEBWi = EzeBestWindkraft.objects.all()
# 	context = {'allEBWi' : allEBWi }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)

# def ezeneufotoindex(request):
# 	allENFi = EzeNeuFotovoltaic.objects.all()
# 	context = {'allENFi' : allENFi }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)

# def ezebestfotoindex(request):
# 	allEBFi = EzeBestFotovoltaic.objects.all()
# 	context = {'allEBFi' : allEBFi }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)

# def ezeneugenindex(request):
# 	allENGi = EzeNeuGenerator.objects.all()
# 	context = {'allENGi' : allENGi }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)

# def ezebestgenindex(request):
# 	allEBGi = EzeBestGenerator.objects.all()
# 	context = {'allEBGi' : allEBGi }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)


# def ezetestindex(request):
# 	allEBGi = EzeBestGenerator.objects.all()
# 	context = {'allEBGi' : allEBGi }
# 	#CHANGE IT!
# 	return render(request, 'certification82/ezeneuwindindex.html', context)

################################################################################
