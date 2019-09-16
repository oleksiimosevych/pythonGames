from django.shortcuts import render
from django.http import HttpResponse
from .models import EzeNeu
	
# Create your views here.
def index(request):
	latest_EzeNeu_list = EzeNeu.objects.order_by('-vDE_EZE1_Name')[:3]
	output = ', '.join([e.vDE_EZE1_Name for e in latest_EzeNeu_list])
	return HttpResponse('Neue Ezes: \n'+output)
#add more views
def detail(request, eZeTyp_id):
	return HttpResponse("You're looking at eZeTyp %s." % eZeTyp_id)

def results(request, eZeTyp_id):
	response = "You're looking at the results of eZeTyp %s."
	return HttpResponse(response % eZeTyp_id)

def vote(request, eZeTyp_id):
	return HttpResponse("You're voting on eZeTyp %s." % eZeTyp_id)