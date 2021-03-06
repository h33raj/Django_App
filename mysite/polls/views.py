# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.core import serializers


from .models import Choice, Question, Document
from .forms import DocumentForm
from django.contrib.auth import login, authenticate
from .models import SignUpForm

import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

# Create your views here.
log = logging.getLogger(__name__)

@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):

    ip = request.META.get('REMOTE_ADDR')
    log.debug('login user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):

    ip = request.META.get('REMOTE_ADDR')

    log.debug('logout user: {user} via ip: {ip}'.format(
        user=user,
        ip=ip
    ))

@receiver(user_login_failed)
def user_login_failed_callback(sender, credentials, **kwargs):

    log.warning('logout failed for: {credentials}'.format(
        credentials=credentials,
    ))

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form': form})

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	response = render(request, 'polls/index.html', context)
	request.session.set_test_cookie()
	#XMLSerializer = serializers.get_serializer('xml')
	#XMLSerializer = serializers.get_serializer("xml")	 
	#xml_serializer = XMLSerializer()
	#with open("file.xml", "w") as out:
	#		xml_serializer.serialize(Question.objects.all(), stream=out)
	#data = xml_serializer.getvalue()
	return response

def simple_upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, 'polls/simple_upload.html', {
			'uploaded_file_url': uploaded_file_url
		})
	return render(request, 'polls/simple_upload.html')	

def model_form_upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = DocumentForm()
	return render(request, 'polls/model_form_upload.html', {
		'form': form
	})

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
	
def results(request, question_id):
		question = get_object_or_404(Question, pk=question_id)
		return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
	# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('results', args=(question.id,)))
