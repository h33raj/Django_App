from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	# ex: /polls/
	url (r'^$', views.index, name='home'),
	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^upload/$', views.model_form_upload, name='upload'),
    url(r'^login/$', auth_views.login, {'template_name': 'polls/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
	url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]

