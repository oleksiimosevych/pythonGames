from django.shortcuts import render
from django.http import HttpResponse
from .models import EzeNeu, EzeBestand, Project
	
# Create your views here.
def index(request):
	project_name = Project.objects.order_by('-project_name')[:3]
	latest_EzeNeu_list = EzeNeu.objects.order_by('-vDE_EZE1_Name')[:3]
	eze_Neus = ', '.join([e.vDE_EZE1_Name for e in latest_EzeNeu_list])
	project_Names = ', '.join([p.project_name for p in project_name])
	return HttpResponse(project_Names+'\n\n<br> Neue Ezes: \n'+eze_Neus )
#add more views
def detail(request, eZeTyp_id):
	return HttpResponse("You're looking at eZeTyp %s." % eZeTyp_id)

def results(request, eZeTyp_id):
	response = "You're looking at the results of eZeTyp %s."
	return HttpResponse(response % eZeTyp_id)

def vote(request, eZeTyp_id):
	return HttpResponse("You're voting on eZeTyp %s." % eZeTyp_id)

def ezenues(request):
	# project_name = Project.objects.order_by('-project_name')[:3]
	latest_EzeNeu_list = EzeNeu.objects.order_by('-vDE_EZE1_Name')[:3]
	eze_Neus = ', '.join([e.vDE_EZE1_Name for e in latest_EzeNeu_list])
	# project_Names = ', '.join([p.project_name for p in project_name])
	return HttpResponse('<br> Neue Ezes: \n'+eze_Neus )

def ezebestands(request):
	# project_name = Project.objects.order_by('-project_name')[:3]
	latest_EzeBestand_list = EzeBestand.objects.order_by('-vDE_EZE_Name_ALT')[:3]
	eze_Bestands = ', '.join([e.vDE_EZE_Name_ALT for e in latest_EzeBestand_list])
	# project_Names = ', '.join([p.project_name for p in project_name])
	return HttpResponse('\n\n<br> Ezes Bestand: \n'+eze_Bestands )
