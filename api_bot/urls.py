"""api_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from profiles import views as profile_views
from twitter import views as twitter_views
from tumblr import views as tumblr_views




urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^register/',profile_views.register),
	url(r'^login/',profile_views.login),
	url(r'^logout/',profile_views.logout),
	url(r'^key/tumblr/create$', profile_views.tumblr_key, name='Tumblr_key'),
	url(r'^key/twitter/create$', profile_views.twitter_key, name='Twitter_key'),

	url(r'^twitter/$',twitter_views.trend),
	url(r'^twitter/user$',twitter_views.Twitter_User),
	url(r'^twitter/follow/$',twitter_views.twitter_fallow, name='Twitter_follow'),
	url(r'^twitter/add/username$',twitter_views.Twitter_User, name='Twitter_User'),
	url(r'^twitter/rt/$',twitter_views.Rt_fallow, name='Twitter_rt'),
	url(r'^twitter/add/rt$',twitter_views.Twitter_Rt, name='Twitter_rtadd'),
	url(r'^twitter/add/unf$',twitter_views.unfollow, name='Twitter_unfollow'),


	url(r'^tumblr/like$',tumblr_views.get_like, name='Tumblr_Like'),
	url(r'^tumblr/add/img$',tumblr_views.img_post, name='Tumblr_imgpost'),
	url(r'^tumblr/add/rt$',tumblr_views.rt_get, name='Tumblr_rtput'),
	url(r'^tumblr/add/url/follow$',tumblr_views.url_follow_put,
		name='Tumblr_url_follow'),
	url(r'^tumblr/post/img$',tumblr_views.img_push, name='Tumblr_post'),
	url(r'^tumblr/post/rt$',tumblr_views.rt_push, name='Tumblr_rt_post'),
	url(r'^tumblr/post/add_rt_text$',tumblr_views.rt_text_save, name='Tumblr_rt_text'),
	url(r'^tumblr/post/add_img_text$',tumblr_views.img_text_save, name='Tumblr_img_text'),






	url(r'^$',profile_views.home)

]