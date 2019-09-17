#rendering possible
from django.shortcuts import render
#add 404
from django.http import Http404
from django.http import HttpResponse
from .models import EzeNeu, EzeBestand, Project
from django.template import loader
	
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
	try:
		latest_EzeNeu_list = EzeNeu.objects.get(pk=project_id)
	except EzeNeu.DoesNotExist:
		raise Http404("No Eze with this project number: "+str(project_id))
	
	context = {	'latest_EzeNeu_list': latest_EzeNeu_list, }
	
	return render(request, 'certification82/details.html', {'latest_EzeNeu_list' : latest_EzeNeu_list})

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
