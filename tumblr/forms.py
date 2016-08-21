from django import forms
from .models import Like_Limit,Img_Post,Img_Content,Rt_Put,Rt_Push
from django.contrib.auth.models import User

class Like(forms.ModelForm):

	class Meta:
		model  = Like_Limit
		fields = ('like',)

class Img_Post_Get(forms.ModelForm):

	class Meta:
		model  = Img_Post
		fields = ('urllink',)

class Img_Post_Push(forms.ModelForm):


	class Meta:
		model  = Img_Content
		fields = ('blogname','context','tag',) 

class Rt_Post_Put(forms.ModelForm):

	class Meta:
		model = Rt_Put
		fields = ('rtlink',)


class Rt_Post_Push(forms.ModelForm):

	class Meta:
		model = Rt_Push
		fields = ('blogname','context',)


class Rt_Text_Post(forms.Form):
	rt_blogname = forms.CharField(label='blog', max_length=200)



class Url_Follow(forms.Form):
	urlname = forms.CharField(label='Url', max_length=200)