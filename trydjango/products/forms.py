from django import forms
from .models import Product
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)

class ProductForm(forms.Form):
	name  	 = forms.CharField()
	username = forms.CharField()
	password = forms.CharField()
	category = forms.CharField()
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	def clean(self, *args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")
		if username and password:
			user_qs = Product.objects.filter(username=username,password=password)
		if user_qs.count() == 1:
			user=user_qs.first()
		else :
			raise forms.ValidationError("Login Invalid")
		return super(UserLoginForm, self).clean(*args,**kwargs)