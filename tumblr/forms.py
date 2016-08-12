from django import forms
from .models import Like_Limit

class Like(forms.ModelForm):

	class Meta:
		model = Like_Limit
		fields = ('like',)