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
    url(r'^signup/$', views.signup, name='signup'),
	url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'polls/password_reset_form.html'} , name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'polls/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'polls/password_reset_confirm.html'} , name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'polls/password_reset_complete.html'} , name='password_reset_complete'),
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'