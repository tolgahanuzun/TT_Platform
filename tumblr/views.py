#-*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, RequestContext
from django.http import *   
from .forms import Like,Img_Post_f,Img_Post_push,Post_Rt_Put,Post_Rt_Push,T_Url_follow
from .models import Img_Post,Rt_Put
from bs4 import BeautifulSoup
from profiles.models import Profile
import urllib
import re
import pytumblr

def ApiClient(request):
	fields = Profile.objects.get(user=request.user)
	api = pytumblr.TumblrRestClient(fields.consumer_keys,
			fields.consumer_secrets,
			fields.access_tokens,
			fields.access_token_secrets
			)
	return api



def Top_Like(request):

	form = Like()
	if request.method == "POST":

		client = ApiClient(request)
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

		client = ApiClient(request)
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
		form = Img_Post_push(request.POST)
		if form.is_valid():
			client = ApiClient(request)
			Imglists = Img_Post.objects.all()


			try:
				formveri = form.save()
				veri =formveri.context.encode('utf-8')
				print type(veri)
				trues = 0
				for Imglist in Imglists:
					try:
						
						post_id= client.create_photo(formveri.blogname, 
						state="queue",
						tags=formveri.tag.split(","),
						source=Imglist,
						caption=formveri.context.encode('utf-8'),
						format="html",
						)
						
						trues = trues+1
						print Imglist.delete()
						Post_status = client.dashboard(since_id= post_id)
						status =Post_status["meta"]
					except:
						print "error 2"

				return render(request, 'tumblr_add.html', {'imgpush_result': form,'count':trues})

			except:		
				print "error 3"
				return render(request, 'index.html')
		else:
			print "error 3"
			return render(request, 'index.html')

	else:
		return render(request, 'tumblr_add.html', {'imgpush':form })

def Rt_put(request):
	form = Post_Rt_Put()

	if request.method == "POST":
		form = Post_Rt_Put(request.POST)
		if form.is_valid():
			formveri = form.save()
			form = Post_Rt_Put()

			return render(request, 'tumblr_add.html', {'rtform':form})
		else:
			return render(request, 'tumblr_add.html', {'rtform': form})
	else:
		return render(request, 'tumblr_add.html', {'rtform': form})


def Push_Rr(request):

	form = Post_Rt_Push()
	if request.method == "POST":
		form = Post_Rt_Push(request.POST)
		if form.is_valid():
			client = ApiClient(request)
			Rtlists = Rt_Put.objects.all()


			try:
				formveri = form.save()

				trues = 0
				for Rtlist in Rtlists:
					str_list=str(Rtlist)
					
						
					post_ids = str_list.split("/reblog/")[1].split("/")[0] 

					rt_id 	 = str_list.split("/reblog/")[1].split("/")[1].split("?")[0]
					print rt_id,post_ids

					post_id= client.reblog(formveri.blogname,
					id=post_ids,
					reblog_key=rt_id,
					comment=formveri.context.encode('utf-8')
					)

					trues = trues+1
					print Rtlist.delete()
					

				
				return render(request, 'tumblr_add.html', {'rtpush_result': form,'count':trues})

			except:		
				print "error 4"
				return render(request, 'index.html')
		else:
			print "error 3"
			return render(request, 'index.html')

	else:
		return render(request, 'tumblr_add.html', {'rtpush':form })

def URL_Follow(request):

	form = T_Url_follow()
	if request.method == "POST":
		
		client = ApiClient(request)
		form = T_Url_follow(request.POST)
		follow_url_link = []
		if form.is_valid():
			
			urlname = request.POST.get('urlname')
			
			htmlcode = urllib.urlopen(urlname).read()
			soup = BeautifulSoup(htmlcode, 'html.parser')
		
			urls = []

			for tag in soup.find_all("a",{"class":"tumblelog"}):
				urls.append(tag['href'])

			lop = soup.find_all("li",class_="like")
			for hop in lop:
				urls.append(hop.find("a")['href'])

			i=1
			for url in urls:
				list_data = client.follow(url)
				follow_url_link.append(url)

			return render(request, 'tumblr_add.html', {'url_rest':urls})
		else:
			return render(request, 'tumblr_add.html', {'url_follow': form})
	else:
		return render(request, 'tumblr_add.html', {'url_follow': form})



