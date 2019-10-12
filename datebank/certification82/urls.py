from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView # new
from . import views
#namespacing paths
app_name = 'certification82'
urlpatterns = [
    #!@#$
    
    # path('', views.index, name='index'),
    #A-Z
    #A
    path('ai_pro<int:projekt_nr>/show', views.allgeminfo, name='allgeminfo'),
    #B
    #All for betreiber
    path('betreibers/all', views.BetreiberIndexView.as_view(), name='betreiberindex'),
    path('new_betr', views.new_betreiber,name = 'new_betreiber'),
    path('betr/update/<int:pk>', views.BetreiberUpdate.as_view(), name='betreiber_update'),
    path('betr/delete/<int:pk>', views.BetreiberDelete.as_view(), name='betreiber_delete'),
    path('betreiber/number/<int:pk>', views.BetreiberDetailView.as_view(), name = 'betreiberdetailview'),
    
    ###best
    path('bestwind/all', views.BestWindkraftIndexView.as_view(), name='ezebestwindindex'),
    path('bestfoto/all', views.BestFotovoltaicIndexView.as_view(), name='ezebestfotoindex'),
    path('bestgen/all', views.BestGeneratorIndexView.as_view(), name='ezebestgenindex'),
        
    #D
    #DOCUMENTS ALL:
    path('alldocs/', views.DocumentIndexView.as_view(), name='documenteindex'),
    path('doc/number/<int:pk>', views.DocumentDetailView.as_view(), name = 'documentdetailview'),

    path('neugen/number/<int:pk>', views.NeuGeneratorDetailView.as_view(), name = 'ezeneugendetail'),
    # the 'name' value as called by the {% url %} template tag the DETAIL of the spec proj use id
    path('detail<int:project_id>765525', views.detail, name='detail'),
    
    #E
    #eze
    path('eze/number/<int:pk>', views.EzeDetailView.as_view(), name = 'ezedetailview'),
    
    path('eze/update/<int:pk>', views.EzeUpdate.as_view(), name='eze_update'),
    path('eze/delete/<int:pk>', views.EzeDelete.as_view(), name='eze_delete'),
    path('<int:ezeneu_id>/show', views.eze_neu_show, name='eze_neu_show'),
    # path('ezebestdetails/<int:ezebest_id>/', views.eze_best_show, name='eze_best_show'),

    #N
    #NETZBETREIBER HERE:
    path('new_netzbet', views.new_netzbetreiber,name = 'new_netzbetreiber'),
    
    path('new_eze_bestand', views.new_eze_bestand, name = 'new_eze_bestand'),
    path('new_eze_neu', views.new_eze_neu, name = 'new_eze_neu'),
    path('new_eze_typ', views.new_eze_typ, name = 'new_eze_typ'),
    path('new_hersteller', views.new_hersteller, name = 'new_hersteller'),
    
    path('neuwind/all', views.NeuWindkraftIndexView.as_view(), name='ezeneuwindindex'),
    path('neufoto/all', views.NeuFotovoltaicIndexView.as_view(), name='ezeneufotoindex'),
    path('neugen/all', views.NeuGeneratorIndexView.as_view(), name='ezeneugenindex'),
    
    #O
    #OF THE PROJECT using id
    # path('ezebestands/', views.ezebestands, name='ezebestands'),
    path('ezeneuwindofproj/<int:project_number>/index', views.ezeneuwindkraftsoftheprojectindex, name='ezeneuwindkraftsoftheprojectindex'),
    path('ezeneufotooftheproj/<int:project_id>/index', views.ezeneufotooftheprojectindex, name='ezeneufotooftheprojectindex'),
    path('ezeneugenoftheproj/<int:project_id>/index', views.ezeneugenoftheprojectindex, name='ezeneugenoftheprojectindex'),
    path('ezebestwindoftheproj/<int:project_id>/index', views.ezebestwindoftheprojectindex, name='ezebestwindoftheprojectindex'),
    path('ezebestfotooftheproj/<int:project_id>/index', views.ezebestfotooftheprojectindex, name='ezebestfotooftheprojectindex'),
    path('ezebestgenoftheproj/<int:project_id>/index', views.ezebestgenoftheprojectindex, name='ezebestgenoftheprojectindex'),
    
    #L
    path('login', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    
    #P
    #PROJECT ALL Links:
    path('', views.IndexView.as_view(), name='index'),
    path('pro<int:project_id>/show', views.project_show, name='project_show'),
    path('pro/update/<int:pk>', views.ProjectUpdate.as_view(), name='project_update'),
    path('pro/delete/<int:pk>', views.ProjectDelete.as_view(), name='project_delete'),
    path('new_projekt', views.new_projekt, name = 'new_projekt'),

    path('pro/number/<int:pk>', views.ProjectDetailView.as_view(), name = 'projectdetailview'),
    
    
    #R
    #RESULTS (about test voting) ex: /polls/5/results/
    path('<int:project_id>/results/', views.results, name='results'),
    
    #V
    # ex: /polls/5/vote/
    path('<int:project_id>/vote/', views.vote, name='vote'),

    #Z
    #ZERTIFIKATINHABER ALL:
    path('new_zert', views.new_zert,name = 'new_zert'),
    # path('zer/update/<int:pk>', views.ZertifikatinhaberUpdate.as_view(), name='zert_update'),
    # path('zer/delete/<int:pk>', views.ZertifikatinhaberDelete.as_view(), name='zert_delete'),
    

    #############################new
    ###docs, betreibers, schutzs, trafos, regelungs list and details
    

    path('schutz/', views.schutzindex, name='schutzindex'),
    # path('schutz/number/<int:pk>', views.SchutzDetailView.as_view(), name = 'documentdetailview'),

    path('trafos/', views.TransformatorIndexView.as_view(), name='trafoindex'),
    path('trafo/number/<int:pk>', views.TransformatorDetailView.as_view(), name = 'transformatordetailview'),

    path('regelungindex/', views.regelungindex, name='regelungindex'),
    # path('regel/number/<int:pk>', views.RegelungDetailView.as_view(), name = 'documentdetailview'),

    



    ###wind, foto, generator
    # path('ezebestwindindex/', views.BestWindkraftIndexView.as_view(), name='ezebestwindindex'),
    # path('ezeneufotoindex/', views.ezeneufotoindex, name='ezeneufotoindex'),
    # path('ezebestfotoindex/', views.ezebestfotoindex, name='ezebestfotoindex'),
    # path('ezeneugenindex/', views.ezeneugenindex, name='ezeneugenindex'),
    # path('ezebestgenindex/', views.ezebestgenindex, name='ezebestgenindex'),
    ##NO NEED for this i hope will be after if b==b
    path('bestfoto/number/<int:pk>', views.BestFotovoltaicDetailView.as_view(), name = 'ezebestfotodetail'),
    path('bestgen/number/<int:pk>', views.BestGeneratorDetailView.as_view(), name = 'ezebestgendetail'),
    path('ezeneuwind/', views.NeuWindkraftIndexView.as_view(), name='ezeneuwindindex'),
    path('neuwind/number/<int:pk>', views.NeuWindkraftDetailView.as_view(), name = 'ezeneuwinddetail'),
    path('bestwind/number/<int:pk>', views.BestWindkraftDetailView.as_view(), name = 'ezebestwinddetail'),
    path('neufoto/number/<int:pk>', views.NeuFotovoltaicDetailView.as_view(), name = 'ezeneufotodetail'),
    

]