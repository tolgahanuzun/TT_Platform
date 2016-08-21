from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, RequestContext
from django.http import *   
from models import Populer,Rt_Kullanicimodel,Unf_model
from profiles.models import Profile
from .forms import Pupuler_Kullanici,Kac_Kullan,Rt_Kullan,Rt_Kullanici,Unf_form
import tweepy
import time
import json

def twitter_api(request):
	fields = Profile.objects.get(user=request.user)
	
	auth = tweepy.OAuthHandler(fields.twitter_consumer_keys, 
		fields.twitter_consumer_secrets)
	auth.set_access_token(fields.twitter_access_tokens, 
		fields.twitter_access_token_secrets)

	return tweepy.API(auth)


def Twitter_User(request):
	form = Pupuler_Kullanici()
	if request.method == "POST":
		form = Pupuler_Kullanici(request.POST)
		if form.is_valid():
				formveri = form.save()
				form = Pupuler_Kullanici()
				return render(request, 'twitter_fallow_add.html', {'form': form})   
	else:
		return render(request, 'twitter_fallow_add.html', {'form': form})

def twitter_fallow(request):
	form = Kac_Kullan()
	if request.method == "POST":
		form = Kac_Kullan(request.POST)

		if form.is_valid():
			formveri = form.save()
			api = twitter_api(request)
			backusers = []
			Userlist = Populer.objects.all()

			for tw_user in Userlist:
				try:
					fallow_list = api.followers_ids(tw_user)
					for x in range(formveri.insan_limiti):
						try:
							api.create_friendship(fallow_list[x])			
							nametw = api.get_user(fallow_list[x])
							backusers.append(nametw.screen_name)
						except:
							print "error"
				except:
					print "error"	
							
			return render(request,'twitter.html',{
			'backusers': backusers
			})

	else:
		return render(request, 'twitter.html', {'form': form})
	
def Twitter_Rt(request):
	form = Rt_Kullanici()
	if request.method == "POST":
		form = Rt_Kullanici(request.POST)
		formveri = form.save()
		form = Rt_Kullanici()
		return render(request, 'twitter_rt_add.html', {'form': form}) 
	else:
		return render(request, 'twitter_rt_add.html', {'form': form})

def Rt_fallow(request):
	form2 = Rt_Kullan()
	if request.method == "POST":
		form2 = Rt_Kullan(request.POST)

		if form2.is_valid():
			formveri = form2.save()
			api = twitter_api(request)
			print formveri.rt_limiti
			rtusers = []
			Rt_lists = Rt_Kullanicimodel.objects.all()
			for rt_list in Rt_lists:
				veriler = api.retweets(rt_list,formveri.rt_limiti)
				for x in range(formveri.rt_limiti):
					tweet =veriler[x]
					user = tweet.user
					try:
						sonuc = api.create_friendship(user.id)
						rtusers.append(user.screen_name)
					except:
						print "No user"

		return render(request,'twitter.html',{
			'rtusers': rtusers
			})
	else:
		return render(request,'twitter.html',{
			'form2': form2
			})

def unfollow(request):
	form3 = Unf_form()
	if request.method == "POST":
		form3 = Unf_form(request.POST)

		if form3.is_valid():
			unfusers = []
			try:	
				formveri = form3.save()
				api = twitter_api(request)
				friends = api.friends_ids()
				for x in range(formveri.unf):
					try:
						users = api.get_user(friends[x])
						api.destroy_friendship(users.screen_name)
						unfusers.append(users.screen_name)
						if (x%50 == 0):
							print "...."
							time.sleep(10)
					except:
						unfusers.append("Error")
			except:
				unfusers.append("Error")

			return render(request,'twitter_add.html',{'unfusers': unfusers})
		else:
			return render(request,'twitter_add.html',{'form3': form3})
	else:
		return render(request,'twitter_add.html',{'form3': form3})


def trend(request):
	api = twitter_api(request)
	c_id= 23424969
	trends= api.trends_place(c_id)
	data = trends[0]
	trends = data['trends']
	
	return render(request,'twitter.html',{
	'trends': trends
	})
