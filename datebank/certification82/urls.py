from django.urls import path

from . import views
#namespacing paths
app_name = 'certification82'
urlpatterns = [
    path('ezedetails/<int:eze_id>/', views.eze_neu_detail, name='eze_neu_detail'),
    path('', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('<int:project_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:project_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:project_id>/vote/', views.vote, name='vote'),

	path('ezenues/', views.ezenues, name='ezenues'),
	path('ezebestands/', views.ezebestands, name='ezebestands'),
	

]