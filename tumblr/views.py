#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, RequestContext
from django.http import *   
from .forms import Like,Img_Post_f,Img_Post_push
from .models import Img_Post
from bs4 import BeautifulSoup
from profiles.models import Profile
import urllib
import re
import pytumblr



def Top_Like(request):

	form = Like()
	if request.method == "POST":
		fields = Profile.objects.get(user=request.user)

		client = pytumblr.TumblrRestClient(fields.consumer_keys,
			fields.consumer_secrets,
			fields.access_tokens,
			fields.access_token_secrets
			)

		form = Like(request.POST)
		like_user = []
		if form.is_valid():
			formdata = form.save()
			try:
				Dashboard = client.dashboard(limit=formdata.like)
				Data = Dashboard["posts"]
				try:
					for likes in range(0,formdata.like):
						Data_key = Data[likes]["reblog_key"]
						Data_id  = Data[likes]["id"]
						list_like = client.like(Data_id, Data_key)
						like_user.append(Data[likes]["blog"]["name"])
						
					return render(request, 'tumblr.html', {'like_user': like_user})
				except:
					error = "For Error"
			except:
				error = "Client Error"	
		else:
			error = "Valid Error"
		return render(request,'tumblr.html',{'error': error})
	else:
		return render(request, 'tumblr_add.html', {'form': form})

def Img_Posts(request):

	form = Img_Post_f()
	if request.method == "POST":
		client = pytumblr.TumblrRestClient(fields.consumer_keys,
			fields.consumer_secrets,
			fields.access_tokens,
			fields.access_token_secrets
			)

		form = Img_Post_f(request.POST)
		status_post = []
		if form.is_valid():
			formveri = form.save()
			form = Img_Post_f()
			return render(request, 'tumblr_add.html', {'imgform':form})
		else:
			return render(request, 'tumblr_add.html', {'imgform': form})
	else:
		return render(request, 'tumblr_add.html', {'imgform': form})

def Push_Img(request):

	form = Img_Post_push()
	if request.method == "POST":
		client = pytumblr.TumblrRestClient(fields.consumer_keys,
			fields.consumer_secrets,
			fields.access_tokens,
			fields.access_token_secrets
			)
		Imglists = Img_Post.objects.all()
		true = 0
		try:
			for Imglist in Imglists:
				try:
					post_id= client.create_photo('blogname', 
					state="queue",
					tags=["tag"],
					source=Imglist,
					caption="""html kod""",
					format="html",
					)
					print Imglist.delete()
					Post_status = client.dashboard(since_id= post_id)
					status =Post_status["meta"]
					true = true+1
				except:
					print "error 2"

			return render(request, 'tumblr_add.html', {'imgpush_result': form,'count':true})

		except:		
			print "error 3"
			return render(request, 'index.html')

	else:
		return render(request, 'tumblr_add.html', {'imgpush':form })
