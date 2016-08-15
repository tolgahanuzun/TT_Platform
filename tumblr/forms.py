from django import forms
from .models import Like_Limit,Img_Post

class Like(forms.ModelForm):

	class Meta:
		model  = Like_Limit
		fields = ('like',)

class Img_Post_f(forms.ModelForm):

	class Meta:
		model  = Img_Post
		fields = ('urllink',)

class Img_Post_push(forms.Form):
	 comment = forms.CharField()
