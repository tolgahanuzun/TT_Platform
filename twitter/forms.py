from django import forms
from .models import Populer,Kac_Kullanici,Rt_Kullanicimodel,Rt_Kacmodel,Unf_model

class Pupuler_Kullanici(forms.ModelForm):

	class Meta:
		model = Populer
		fields = ('twitter_name',)

class Kac_Kullan(forms.ModelForm):

	class Meta:
		model = Kac_Kullanici
		fields = ('insan_limiti',)

class Rt_Kullanici(forms.ModelForm):

	class Meta:
		model = Rt_Kullanicimodel
		fields = ('rt_name',)

class Rt_Kullan(forms.ModelForm):

	class Meta:
		model = Rt_Kacmodel
		fields = ('rt_limiti',)


class Unf_form(forms.ModelForm):

	class Meta:
		model = Unf_model
		fields = ('unf',)



