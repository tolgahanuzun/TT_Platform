from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core.files.base import ContentFile
from django.db.models import Q
from django.http import *
from profiles.models import Profile

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)

	def clean(self):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if not username or not password:
			return self.cleaned_data

		user = authenticate(username=username,
							password=password)

		if user:
			self.user = user
		else:
			raise ValidationError("Error!")

		return self.cleaned_data    

class RegistrationForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ("first_name", "last_name", "username", "email", "password1", "password2")
	 
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)

		if commit:
			user.save()
		
		return user


class Tumblr_Key_Create(forms.Form):
	tumblr_consumer_keys = forms.CharField(label=u"Tumblr Consumer keys", required=True)
	tumblr_consumer_secrets = forms.CharField(label=u"Tumblr Consumer secrets", required=True)
	tumblr_access_tokens = forms.CharField(label=u"Tumblr Access Tokens", required=True)
	tumblr_access_token_secrets = forms.CharField(label=u"Tumblr Access token_secrets", required=True)


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(Tumblr_Key_Create, self).__init__(*args, **kwargs)

	def change(self):
		user_profile = Profile.objects.get(user=self.user)
		data = self.cleaned_data
	
		user_profile.profile = self.user
		user_profile.tumblr_consumer_keys = data.get("tumblr_consumer_keys")
		user_profile.tumblr_consumer_secrets = data.get("tumblr_consumer_secrets")
		user_profile.tumblr_access_tokens = data.get("tumblr_access_tokens")
		user_profile.tumblr_access_token_secrets = data.get("tumblr_access_token_secrets")

		user_profile.save()

		return self.user

class Twitter_Key_Create(forms.Form):
	twitter_consumer_keys = forms.CharField(label=u"Twitter Consumer keys", required=True)
	twitter_consumer_secrets = forms.CharField(label=u"Twitter Consumer secrets", required=True)
	twitter_access_tokens = forms.CharField(label=u"Twitter Access Tokens", required=True)
	twitter_access_token_secrets = forms.CharField(label=u"Twitter Access token_secrets", required=True)


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(Twitter_Key_Create, self).__init__(*args, **kwargs)

	def change(self):
		user_profile = Profile.objects.get(user=self.user)
		data = self.cleaned_data
		
		user_profile.profile = self.user
		user_profile.twitter_consumer_keys = data.get("twitter_consumer_keys")
		user_profile.twitter_consumer_secrets = data.get("twitter_consumer_secrets")
		user_profile.twitter_access_tokens = data.get("twitter_access_tokens")
		user_profile.twitter_access_token_secrets = data.get("twitter_access_token_secrets")

		user_profile.save()

		return self.user