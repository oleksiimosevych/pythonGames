from django.urls import path

from . import views
#namespacing paths
app_name = 'certification82'
urlpatterns = [
    path('<int:ezeneu_id>/show', views.eze_neu_show, name='eze_neu_show'),
    # path('ezebestdetails/<int:ezebest_id>/', views.eze_best_show, name='eze_best_show'),
    
    ## GENERIC indexes 
    path('', views.IndexView.as_view(), name='index'),
    ###new
    path('neuwind/all', views.NeuWindkraftIndexView.as_view(), name='ezeneuwindindex'),
    path('neufoto/all', views.NeuFotovoltaicIndexView.as_view(), name='ezeneufotoindex'),
    path('neugen/all', views.NeuGeneratorIndexView.as_view(), name='ezeneugenindex'),
    ###best
    path('bestwind/all', views.BestWindkraftIndexView.as_view(), name='ezebestwindindex'),
    path('bestfoto/all', views.BestFotovoltaicIndexView.as_view(), name='ezebestfotoindex'),
    path('bestgen/all', views.BestGeneratorIndexView.as_view(), name='ezebestgenindex'),
    
    # the 'name' value as called by the {% url %} template tag the DETAIL of the spec proj use id
    path('detail<int:project_id>', views.detail, name='detail'),
    ##############
    
    # ex: /polls/5/results/
    path('<int:project_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:project_id>/vote/', views.vote, name='vote'),
    #???
	path('ezeneuwind/', views.NeuWindkraftIndexView.as_view(), name='ezeneuwindindex'),
    path('neuwind/number/<int:pk>', views.NeuWindkraftDetailView.as_view(), name = 'ezeneuwinddetail'),
    path('bestwind/number/<int:pk>', views.BestWindkraftDetailView.as_view(), name = 'ezebestwinddetail'),
    path('neufoto/number/<int:pk>', views.NeuFotovoltaicDetailView.as_view(), name = 'ezeneufotodetail'),
    path('bestfoto/number/<int:pk>', views.BestFotovoltaicDetailView.as_view(), name = 'ezebestfotodetail'),
    
    

######OF THE PROJECT using id
	# path('ezebestands/', views.ezebestands, name='ezebestands'),
    path('ezeneuwindofproj/<int:project_id>/index', views.ezeneuwindkraftsoftheprojectindex, name='ezeneuwindkraftsoftheprojectindex'),
    path('ezeneufotooftheproj/<int:project_id>/index', views.ezeneufotooftheprojectindex, name='ezeneufotooftheprojectindex'),
    path('ezeneugenoftheproj/<int:project_id>/index', views.ezeneugenoftheprojectindex, name='ezeneugenoftheprojectindex'),
    path('ezebestwindoftheproj/<int:project_id>/index', views.ezebestwindoftheprojectindex, name='ezebestwindoftheprojectindex'),
    path('ezebestfotooftheproj/<int:project_id>/index', views.ezebestfotooftheprojectindex, name='ezebestfotooftheprojectindex'),
    path('ezebestgenoftheproj/<int:project_id>/index', views.ezebestgenoftheprojectindex, name='ezebestgenoftheprojectindex'),
    
  
    #############################new
    ###docs, betreibers, schutzs, trafos, regelungs
    path('alldocs/', views.documenteindex, name='documenteindex'),
    path('betreibers/', views.betreiberindex, name='betreiberindex'),
    path('schutz/', views.schutzindex, name='schutzindex'),
    path('trafos/', views.trafoindex, name='trafoindex'),
    path('regelungindex/', views.regelungindex, name='regelungindex'),
    
    ###wind, foto, generator
    # path('ezebestwindindex/', views.BestWindkraftIndexView.as_view(), name='ezebestwindindex'),
    # path('ezeneufotoindex/', views.ezeneufotoindex, name='ezeneufotoindex'),
    # path('ezebestfotoindex/', views.ezebestfotoindex, name='ezebestfotoindex'),
    # path('ezeneugenindex/', views.ezeneugenindex, name='ezeneugenindex'),
    # path('ezebestgenindex/', views.ezebestgenindex, name='ezebestgenindex'),


]