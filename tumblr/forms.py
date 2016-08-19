from django import forms
from .models import Like_Limit,Img_Post,Img_Content,Rt_Put,Rt_Push

class Like(forms.ModelForm):

	class Meta:
		model  = Like_Limit
		fields = ('like',)

class Img_Post_f(forms.ModelForm):

	class Meta:
		model  = Img_Post
		fields = ('urllink',)

class Img_Post_push(forms.ModelForm):


	class Meta:
		model  = Img_Content
		fields = ('blogname','context','tag',) 

class Post_Rt_Put(forms.ModelForm):

	class Meta:
		model = Rt_Put
		fields = ('rt_link',)


class Post_Rt_Push(forms.ModelForm):

	class Meta:
		model = Rt_Push
		fields = ('blogname','context',)

class T_Url_follow(forms.Form):
    urlname = forms.CharField(label='Url', max_length=200)