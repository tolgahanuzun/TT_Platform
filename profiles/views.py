from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.core.exceptions import ValidationError
from django.http import *
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from profiles.forms import LoginForm, RegistrationForm, Tumblr_Key_Create,Twitter_Key_Create
from profiles.models import Profile
from django.utils import timezone

def login(request):
	if not request.user.is_authenticated():
		context = {}
		try:
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user is not None:
				auth_login(request, user)
				return HttpResponseRedirect("/")
			else:
				context['error'] = 'Non active user'
				
		except:
			context['error'] = ''

		populateContext(request, context)
		return render(request, 'login.html', context)

	else:
		return HttpResponseRedirect("/")

def logout(request):
	context = {}
	try:
		auth_logout(request)
		return HttpResponseRedirect("/")
	except:
		context['error'] = 'Some error occured.'
	
	populateContext(request, context)
	return render(request, 'login.html', context)

def populateContext(request, context):
	context['authenticated'] = request.user.is_authenticated()

	if context['authenticated'] == True:
		context['username'] = request.user.username



def register(request): 
	if not request.user.is_authenticated():
		form = RegistrationForm()

		if request.method == "POST":
			form = RegistrationForm(request.POST)

			if  form.is_valid():
				form.save()       
				return render(request,"login.html",
								   locals())
			else:
				form = RegistrationForm()
				return render(request,"register.html",
								   locals())
		else:
			form = RegistrationForm()
			return render(request, "register.html",{'form':form})

	else:
		return HttpResponseRedirect("/")    

def home(request):
	if request.user.is_authenticated():
		currentTime = timezone.localtime(timezone.now())
		return render(request, "index.html", 
					  {'currentTime':currentTime})
	else:
		return render(request, "index.html")

def tumblr_key(request):
	if request.user.is_authenticated():
		form = Tumblr_Key_Create()

		if request.method == "POST":
			form = Tumblr_Key_Create(request.POST, user=request.user)

			if form.is_valid():
				form.change()
				return render(request,'user_key.html',{'tumblr_update':""})

			else:
				return render(request,'user_key.html',{'tumblr_form': form})

		else:			
			return render(request,'user_key.html',{'tumblr_form': form})	

	else:
		return render(request,'index.html')

def twitter_key(request):
	if request.user.is_authenticated():
		form = Twitter_Key_Create()

		if request.method == "POST":
			form = Twitter_Key_Create(request.POST, user=request.user)

			if form.is_valid():
				form.change()
				return render(request,'user_key.html',{'twitter_update':""})

			else:
				return render(request,'user_key.html',{'twitter_form': form})

		else:			
			return render(request,'user_key.html',{'twitter_form': form})

	else:
		return render(request,'index.html')




