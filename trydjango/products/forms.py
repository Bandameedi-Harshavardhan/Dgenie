from django import forms
from .models import Product
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)

class ProductForm(forms.Form):
	name  	 = forms.CharField(required=True)
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)
	category = forms.ChoiceField(choices=((1, ("Professor")),(2, ("Student"))),required=True)
	def clean(self, *args,**kwargs):
		username=self.cleaned_data.get("username")
		if username:
			user_qs = Product.objects.filter(username=username)
		if user_qs.count() == 1:
			raise forms.ValidationError("User Already Exists")
		else :
			user=user_qs.first()
		return super(ProductForm, self).clean(*args,**kwargs)
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