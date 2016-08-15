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
		fields = ("first_name", "last_name", "username", "email",  "password1", "password2")
	 
	
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)


		if commit:
			user.save()
		
		return user



class KeyCreateForm(forms.Form):
	first_name = forms.CharField(label=u"First Name", required=True)
	last_name = forms.CharField(label=u"Last Name", required=True)
	consumer_keys = forms.CharField(label=u"Consumer keys", required=True)
	consumer_secrets = forms.CharField(label=u"Consumer secrets", required=True)
	access_tokens = forms.CharField(label=u"Access Tokens", required=True)
	access_token_secrets = forms.CharField(label=u"Access token_secrets", required=True)


	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super(KeyCreateForm, self).__init__(*args, **kwargs)

	def change(self):
		user_profile = Profile.objects.get(user=self.user)
		print 1
		data = self.cleaned_data

		self.user.first_name = data.get("first_name")
		self.user.last_name = data.get("last_name")
		self.user.save()	
		
		user_profile.profile = self.user
		user_profile.consumer_keys = data.get("consumer_keys")
		user_profile.consumer_secrets = data.get("consumer_secrets")
		user_profile.access_tokens = data.get("access_tokens")
		user_profile.access_token_secrets = data.get("access_token_secrets")

		user_profile.save()

		return self.user