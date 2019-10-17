from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView # new
from . import views
#namespacing paths
app_name = 'certification82'
urlpatterns = [
    #!@#$
    path('', views.IndexView.as_view(), name='index'),
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
    path('upload_pdf', views.upload_doc, name = 'upload_doc'),
    
    # path('new_document', views.new_document, name = 'new_document'),
    path('alldocs/', views.DocumentIndexView.as_view(), name='documenteindex'),
    path('doc/number/<int:pk>', views.DocumentDetailView.as_view(), name = 'documentdetailview'),
    path('doc/update/<int:pk>', views.DocumentUpdate.as_view(), name='doc_update'),
    path('doc/delete/<int:pk>', views.DocumentDelete.as_view(), name='doc_delete'),
    

    path('neugen/number/<int:pk>', views.NeuGeneratorDetailView.as_view(), name = 'ezeneugendetail'),
    # the 'name' value as called by the {% url %} template tag the DETAIL of the spec proj use id
    path('detail<int:project_id>765525', views.detail, name='detail'),
    
    #E
    #eze
    path('eze_user_detail<int:projekt_nr>', views.eze_user_detail, name = 'eze_user_detail'),
    path('new_eze_bestand', views.new_eze_bestand, name = 'new_eze_bestand'),
    path('new_eze_neu', views.new_eze_neu, name = 'new_eze_neu'),
    path('eze/number/<int:pk>', views.EzeDetailView.as_view(), name = 'ezedetailview'),
    path('eze/update/<int:pk>', views.EzeUpdate.as_view(), name='eze_update'),
    path('ezes/', views.EzeIndexView.as_view(), name='ezeindex'),
    # path('eze/update2/<int:pk>', views.EzeUpdate.as_view(), name='eze_update2'),
    path('eze/delete/<int:pk>', views.EzeDelete.as_view(), name='eze_delete'),
    path('<int:ezeneu_id>/show', views.eze_neu_show, name='eze_neu_show'),
    # path('ezebestdetails/<int:ezebest_id>/', views.eze_best_show, name='eze_best_show'),

    #EZETYP
    
    path('ezetyp/number/<int:pk>', views.EzeTypDetailView.as_view(), name = 'ezetypdetailview'),
    path('ezetyp/update/<int:pk>', views.EzeTypUpdate.as_view(), name='ezetyp_update'),
    path('ezetyps/', views.EzeTypIndexView.as_view(), name='ezetypindex'),
    path('ezetyp/delete/<int:pk>', views.EzeTypDelete.as_view(), name='ezetyp_delete'),
    
    path('new_eze_typ', views.new_eze_typ, name = 'new_eze_typ'),
    
    
    #N
    #NETZBETREIBER HERE:
    path('netzbet/number/<int:pk>', views.NetzbetreiberDetailView.as_view(), name = 'netzbetreiberdetailview'),
    path('netzbet/all', views.NetzbetreiberIndexView.as_view(), name='netzbetreiberindex'),
    path('new_netzbet', views.new_netzbetreiber,name = 'new_netzbetreiber'),
    path('netzbet/update/<int:pk>', views.NetzbetreiberUpdate.as_view(), name='netzbet_update'),
    # path('eze/update2/<int:pk>', views.EzeUpdate.as_view(), name='eze_update2'),
    path('netzbet/delete/<int:pk>', views.NetzbetreiberDelete.as_view(), name='netzbet_delete'),
    
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
    
    path('pro<int:project_id>/show', views.project_show, name='project_show'),
    path('pro/update/<int:pk>', views.ProjectUpdate.as_view(), name='project_update'),
    path('pro/delete/<int:pk>', views.ProjectDelete.as_view(), name='project_delete'),
    path('new_projekt', views.new_projekt, name = 'new_projekt'),

    path('pro/number/<int:pk>', views.ProjectDetailView.as_view(), name = 'projectdetailview'),
    
    
    #R
    #RESULTS (about test voting) ex: /polls/5/results/
    path('<int:project_id>/results/', views.results, name='results'),
    
    #T

#T
    path('trafoher/update/<int:pk>', views.TrafoHerstellerUpdate.as_view(), name='trafoher_update'),
    path('trafoher/delete/<int:pk>', views.TrafoHerstellerDelete.as_view(), name='trafoher_delete'),
    path('new_trafoher', views.new_trafohersteller,name = 'new_trafohersteller'),
    path('trafoher/all', views.TrafoHerstellerIndexView.as_view(), name='trafoherstellerindex'),
    path('trafoher/number/<int:pk>', views.TrafoHerstellerDetailView.as_view(), name = 'trafoherstellerdetailview'),
    
    path('trafotyp/update/<int:pk>', views.TrafoTypUpdate.as_view(), name='trafotyp_update'),
    path('trafotyp/delete/<int:pk>', views.TrafoTypDelete.as_view(), name='trafotyp_delete'),
    path('new_trafotyp', views.new_trafotyp,name = 'new_trafotyp'),
    path('trafotyps/', views.TrafoTypIndexView.as_view(), name='trafotypindex'),
    path('trafotyp/number/<int:pk>', views.TrafoTypDetailView.as_view(), name = 'trafotypdetailview'),
    
    path('trafo_user_detail<int:projekt_nr>', views.trafo_user_detail, name = 'trafo_user_detail'),
    path('trafo/update/<int:pk>', views.TransformatorUpdate.as_view(), name='trafo_update'),
    path('trafo/delete/<int:pk>', views.TransformatorDelete.as_view(), name='trafo_delete'),
    path('new_trafo', views.new_trafo,name = 'new_trafo'),
    path('trafos/', views.TransformatorIndexView.as_view(), name='trafoindex'),
    path('trafo/number/<int:pk>', views.TransformatorDetailView.as_view(), name = 'transformatordetailview'),
    

    #V
    # ex: /polls/5/vote/
    path('<int:project_id>/vote/', views.vote, name='vote'),

    #Z
    #ZERTIFIKATINHABER ALL:
    path('new_zert', views.new_zert,name = 'new_zert'),
    path('zer/update/<int:pk>', views.ZertifikatsinhaberUpdate.as_view(), name='zert_update'),
    path('zer/delete/<int:pk>', views.ZertifikatsinhaberDelete.as_view(), name='zert_delete'),
    path('zerts/', views.ZertifikatsinhaberIndexView.as_view(), name='zertifikatsinhaberindexview'),
    path('zerts/number/<int:pk>', views.ZertifikatsinhaberDetailView.as_view(), name = 'zertifikatsinhaberdetailview'),
    
    

    #############################new
    ###docs, betreibers, schutzs, trafos, regelungs list and details
    

    path('schutz/', views.schutzindex, name='schutzindex'),
    # path('schutz/number/<int:pk>', views.SchutzDetailView.as_view(), name = 'documentdetailview'),


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