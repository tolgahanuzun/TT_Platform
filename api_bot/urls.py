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



urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
	url(r'^register/',profile_views.register),
	url(r'^login/',profile_views.login),
	url(r'^logout/',profile_views.logout),
	url(r'^twitter/$',twitter_views.trend),
	url(r'^twitter/user$',twitter_views.Twitter_User),
	url(r'^$',profile_views.home)

]