from django.shortcuts import render, get_object_or_404
from django.template import Template, Context, RequestContext
from django.http import *	
import tweepy
import time
import json
from models import Populer

def twitter_api():
	consumer_key = "ny12eTofyvNky84aegDJIyEM3"
	consumer_secret ="g48TGrdxgJKVQptNTUDWZzCUjWHKvaajd2yGUMtbniJFeVIdRJ"
	access_token = "2489791711-caoYca1na4EtA8LYtojzd6Smxeq7udj3dnWGYsj"
	access_token_secret = "70mzq65LPBTlP2nLzAsVt6aYd3cXofYGwLrQWKCGkRBVn"
	 

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	return tweepy.API(auth)



def Twitter_User(request):
	api = twitter_api()
	backusers = []
	Userlist = Populer.objects.all()

	for tw_user in Userlist:
		
		fallow_list = api.followers_ids(tw_user)
		for x in range(10):
			try:
				api.create_friendship(fallow_list[x])			
				nametw = api.get_user(fallow_list[x])
				backusers.append(nametw.screen_name)
			except:
				print "error"

	return render(request,'twitter.html',{
	'backusers': backusers
	})


def trend(request):
	api = twitter_api()
	trends= api.trends_place(23424969)
	data = trends[0]
	trends = data['trends']
	
	return render(request,'twitter.html',{
	'trends': trends
	})
