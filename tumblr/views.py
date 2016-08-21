#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, RequestContext
from django.http import *   
from bs4 import BeautifulSoup
from profiles.models import Profile
from .models import Img_Post,Rt_Put
from .forms import Like,Img_Post_Get,Img_Post_Push,Rt_Post_Put,Rt_Post_Push,Url_Follow
import urllib
import re
import pytumblr

def api_client(request):
	fields = Profile.objects.get(user=request.user)
	api = pytumblr.TumblrRestClient(fields.tumblr_consumer_keys,
			fields.tumblr_consumer_secrets,
			fields.tumblr_access_tokens,
			fields.tumblr_access_token_secrets
			)
	return api

def get_like(request):
	form = Like()
	
	if request.method == "POST":
		client = api_client(request)
		form = Like(request.POST)
		like_user = []
		
		if form.is_valid():
			formdata = form.save()

			try:
				dashboard = client.dashboard(limit=formdata.like)
				data = dashboard["posts"]
				
				try:
					for likes in range(0,formdata.like):
						data_key = data[likes]["reblog_key"]
						data_id  = data[likes]["id"]
						list_like = client.like(data_id, data_key)
						like_user.append(data[likes]["blog"]["name"])

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

def img_post(request):
	form = Img_Post_Get()
	
	if request.method == "POST":
		client = api_client(request)
		form = Img_Post_Get(request.POST)
		status_post = []
		
		if form.is_valid():
			formveri = form.save()
			form = Img_Post_Get()
			return render(request, 'tumblr_add.html', {'imgform':form})
		else:
			return render(request, 'tumblr_add.html', {'imgform': form})

	else:
		return render(request, 'tumblr_add.html', {'imgform': form})

def img_push(request):
	form = Img_Post_Push()
	
	if request.method == "POST":
		form = Img_Post_Push(request.POST)
		
		if form.is_valid():
			client = api_client(request)
			imglists = Img_Post.objects.all()
			
			try:
				formveri = form.save()
				veri =formveri.context.encode('utf-8')
				COUNT = 0
				for imglist in imglists:
						post_id= client.create_photo(formveri.blogname, 
						state="queue",
						tags=formveri.tag.split(","),
						source=imglist,
						caption=formveri.context.encode('utf-8'),
						format="html")
						imglist.delete()
				return render(request, 'tumblr_add.html', {
					'imgpush_result': form,
					'count':COUNT
					})
			except:		
				print "Form Error"
				return render(request, 'index.html')

		else:
			print "Form Valid Error"
			return render(request, 'index.html')

	else:
		return render(request, 'tumblr_add.html', {'imgpush':form })

def rt_get(request):
	form = Rt_Post_Put()

	if request.method == "POST":
		form = Rt_Post_Put(request.POST)

		if form.is_valid():
			form.save()
			form = Rt_Post_Put()
			return render(request, 'tumblr_add.html', {'rtform':form})
		else:
			return render(request, 'tumblr_add.html', {'rtform': form})

	else:
		return render(request, 'tumblr_add.html', {'rtform': form})

def rt_push(request):
	form = Rt_Post_Push()

	if request.method == "POST":
		form = Rt_Post_Push(request.POST)

		if form.is_valid():
			client = api_client(request)
			rtlists = Rt_Put.objects.all()

			try:
				formveri = form.save()
				COUNT = 0
				for rtlist in rtlists:
					rtlist_str = str(rtlist)
					post_ids = rtlist_str.split("/reblog/")[1].split("/")[0] 
					rt_id = rtlist_str.split("/reblog/")[1].split("/")[1].split("?")[0]
					post_id= client.reblog(formveri.blogname,
					id=post_ids,
					reblog_key=rt_id,
					comment=formveri.context.encode('utf-8'))
					COUNT = COUNT+1
					rtlist.delete()
				return render(request, 'tumblr_add.html', {
					'rtpush_result': form,
					'count':COUNT
					})
			except:		
				print "Save or Api Error"
				return render(request, 'index.html')

		else:
			print "Form valid error"
			return render(request, 'index.html')

	else:
		return render(request, 'tumblr_add.html', {'rtpush':form })

def url_follow_put(request):
	form = Url_Follow()

	if request.method == "POST":
		client = api_client(request)
		form = Url_Follow(request.POST)

		if form.is_valid():
			follow_url_link = []
			urlname = request.POST.get('urlname')
			htmlcode = urllib.urlopen(urlname).read()
			soup = BeautifulSoup(htmlcode, 'html.parser')
			urls = []
			for tag in soup.find_all("a",{"class":"tumblelog"}):
				urls.append(tag['href'])
			likes = soup.find_all("li",class_="like")
			for like in likes:
				urls.append(like.find("a")['href'])
			for url in urls:
				list_data = client.follow(url)
				follow_url_link.append(url)
			return render(request, 'tumblr_add.html', {'url_rest':urls})
		else:
			return render(request, 'tumblr_add.html', {'url_follow': form})
			
	else:
		return render(request, 'tumblr_add.html', {'url_follow': form})



