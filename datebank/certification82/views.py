#rendering possible
from django.shortcuts import get_object_or_404, render
#add 404
from django.http import Http404
from django.http import HttpResponse
from .models import EzeNeu, EzeBestand, Project, EzeBestGenerator, EzeBestFotovoltaic, EzeBestWindkraft, Eze, EzeNeuGenerator, EzeNeuWindkraft, EzeNeuFotovoltaic
from django.template import loader
#add pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

	
# Create your views here.
def index(request):
	project_name_list = Project.objects.order_by('-project_creation_date')[:3]
	latest_EzeNeu_list = EzeNeu.objects.order_by('-vDE_EZE1_Name')[:3]
	eze_Neus = ', '.join([e.vDE_EZE1_Name for e in latest_EzeNeu_list])
	# project_Names = ' , '.join([p.project_name for p in project_name])
	#added template
	template = loader.get_template('certification82/index.html')
	context = {	'project_name_list': project_name_list, }
	return render(request, 'certification82/index.html', context)
	# return HttpResponse(project_Names+'\n\n<br> Neue Ezes: \n'+eze_Neus )
#add more views

def detail(request, project_id):
	# try:
	ezen = get_object_or_404(Project, pk = project_id)
	
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
	
	return render(request, 'certification82/detail.html', {'ezen' : ezen })

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
