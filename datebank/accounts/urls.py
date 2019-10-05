from django.urls import path

from . import views as core_views
from django.conf.urls import url
# from mysite.core import views

urlpatterns = [
	# path('signup/', views.SignUp.as_view(), name='signup'),
	url(r'^signup/$', core_views.signup, name='signup'),
]