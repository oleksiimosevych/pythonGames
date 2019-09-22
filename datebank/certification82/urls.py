from django.urls import path

from . import views
#namespacing paths
app_name = 'certification82'
urlpatterns = [
    path('<int:ezeneu_id>/show', views.eze_neu_show, name='eze_neu_show'),
    # path('ezebestdetails/<int:ezebest_id>/', views.eze_best_show, name='eze_best_show'),
    path('', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('<int:project_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:project_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:project_id>/vote/', views.vote, name='vote'),

	# path('ezenues/', views.ezenues, name='ezenues'),
	# path('ezebestands/', views.ezebestands, name='ezebestands'),
	

]