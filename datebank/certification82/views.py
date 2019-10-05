#rendering possible
from django.shortcuts import get_object_or_404, render
#add 404
from django.http import Http404
###or HttpResponseRedirect
from django.http import HttpResponse
from .models import EzeNeu, EzeBestand, Project, EzeBestGenerator, EzeBestFotovoltaic, EzeBestWindkraft, Eze, EzeNeuGenerator, EzeNeuWindkraft, EzeNeuFotovoltaic, Document, TrafoTyp, Transformator, Betreiber, Zertifikatsinhaber, Netzbetreiber#, Schutz, Regelung
from django.template import loader
#add pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic 
from django.urls import reverse
	
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
class IndexView(generic.ListView):
	template_name = 'certification82/index.html'
	context_object_name = 'project_name_list'

	def get_queryset(self):
		# user = get_object_or_404(User, pk=user_id)
		"""Return the last five published questions."""
		# return Project.objects.filter(project_number==user.projekt_Nr)[:5]

		# user= get_object_or_404(Betreiber, betreiber_id=pk)
		# return Project.objects.get(project_number=user.Project_NR)[:5]
		return Project.objects.all
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
class TransformatorIndexView(generic.ListView):
	context_object_name = 'transformator_name_list'
	template_name = 'certification82/list_views/Transformator_list.html'
	def get_queryset(self):
		return Transformator.objects.order_by('-VDE_Trafo')[:5]
class TransformatorDetailView(generic.DetailView):
	model = Transformator
	template_name = 'certification82/detailed_views/Transformator_detail.html'


def regelungindex(request):
	allregelungs = Regelung.objects.all()
	context = {'allregelungs' : allregelungs }
	#CHANGE IT!
	return render(request, 'certification82/ezeneuwindindex.html', context)

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


#good
def ezeneuwindindex(request):
	ezeneuwind = EzeNeuWindkraft.objects.all()
	# ezeneuwind = get_object_or_404(EzeNeuWindkraft, pk = ezeneuwindkraft_id)
	context = {'ezeneuwind' : ezeneuwind }
	return render(request, 'certification82/ezeneuwindindex.html', context)
#???
def ezeneuwindkraftsoftheprojectindex(request, project_id):
	ezeneuwindofpro = get_object_or_404(Project, pk = project_id)
	ezeneuwind = EzeNeuWindkraft.objects.filter(project_id=project_id)
	
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
	ezeneuwind = EzeNeuWindkraft.objects.filter(project_id=project_id)
	ezeneugen = EzeNeuGenerator.objects.filter(project_id=project_id)
	ezeneufotovoltaic = EzeNeuFotovoltaic.objects.filter(project_id=project_id)
	ezebestwindkraft = EzeBestWindkraft.objects.filter(project_id=project_id)
	ezebestfotovoltaic = EzeBestFotovoltaic.objects.filter(project_id=project_id)
	ezebestgenerator = EzeBestGenerator.objects.filter(project_id=project_id)
	allneuezes = {'ezeneuwind': ezeneuwind, 'ezeneugen': ezeneugen, 'ezeneufotovoltaic':ezeneufotovoltaic}
	allbestezes = {'ezebestwindkraft': ezebestwindkraft, 'ezebestgenerator':ezebestgenerator, 'ezebestfotovoltaic': ezebestfotovoltaic}
	# .filter(project_id=project_id)
	context = {'allneuezes' : allneuezes, 'allbestezes' : allbestezes, 'ezen' : ezen, 'ezeneuwind': ezeneuwind, 'ezeneugen': ezeneugen, 'ezeneufotovoltaic':ezeneufotovoltaic, 'ezebestwindkraft': ezebestwindkraft, 'ezebestfotovoltaic': ezebestfotovoltaic, 'ezebestgenerator':ezebestgenerator }
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
	ezeneu1 = get_object_or_404(EzeNeu, pk = ezeneu_id)
	eze_neu_list = EzeNeu.objects.all()	
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
