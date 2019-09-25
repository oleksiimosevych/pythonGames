from django.urls import path

from . import views
#namespacing paths
app_name = 'certification82'
urlpatterns = [
    path('<int:ezeneu_id>/show', views.eze_neu_show, name='eze_neu_show'),
    # path('ezebestdetails/<int:ezebest_id>/', views.eze_best_show, name='eze_best_show'),
    
    ##new GENERIC
    path('', views.IndexView.as_view(), name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('detail<int:project_id>', views.detail, name='detail'),
    ##############
    
    # ex: /polls/5/results/
    path('<int:project_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:project_id>/vote/', views.vote, name='vote'),
    #???
	path('ezeneuwind/', views.ezeneuwindindex, name='ezeneuwindindex'),
	# path('ezebestands/', views.ezebestands, name='ezebestands'),
	path('ezeneuwindofproj/<int:project_id>/index', views.ezeneuwindkraftsoftheprojectindex, name='ezeneuwindkraftsoftheprojectindex'),

    #############################new
    ###docs, betreibers, schutzs, trafos, regelungs
    path('alldocs/', views.documenteindex, name='documenteindex'),
    path('betreibers/', views.betreiberindex, name='betreiberindex'),
    path('schutz/', views.schutzindex, name='schutzindex'),
    path('trafos/', views.trafoindex, name='trafoindex'),
    path('regelungindex/', views.regelungindex, name='regelungindex'),
    
    ###wind, foto, generator
    path('ezebestwindindex/', views.ezebestwindindex, name='ezebestwindindex'),
    path('ezeneufotoindex/', views.ezeneufotoindex, name='ezeneufotoindex'),
    path('ezebestfotoindex/', views.ezebestfotoindex, name='ezebestfotoindex'),
    path('ezeneugenindex/', views.ezeneugenindex, name='ezeneugenindex'),
    path('ezebestgenindex/', views.ezebestgenindex, name='ezebestgenindex'),


]