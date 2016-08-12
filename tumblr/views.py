from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, RequestContext
from django.http import *   
from .forms import Like
from bs4 import BeautifulSoup
import urllib
import re
import pytumblr

def Tumblr_Api():
	api = pytumblr.TumblrRestClient(
  '5fu8uRys780qRTnLeJ7FNvrLBcPR4pN0V0BpVHhAxTCF0zTWF7',
  'bYvbxmeHkLFfqpGOFjfO7vETi1cFUpyOtIdhLImNNkJNZr1Dx7',
  'pnrVKdaZC7XCG0anWKhKA8X9CHMm0Bj4vh3dgsdizV7CgVFsCw',
  'gKDL6Q70D1JlvmS0TZ4jr1zqrwPchI6LubpIU9XDJOQgtpzYgs'
  )
	return api

def Top_Like(request):
	client = Tumblr_Api()
	form = Like()
	if request.method == "POST":
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

