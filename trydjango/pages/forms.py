from django import forms
from .models import Product
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
)

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class AssignmentForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    references = forms.CharField(max_length=100)

class CourseForm(forms.Form):
	course_name = forms.CharField(max_length=100)
	course_id = forms.CharField(max_length=100)
	year = forms.CharField(max_length=100)

class ProductForm(forms.Form):
	name  	 = forms.CharField(required=True)
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)
	category = forms.ChoiceField(choices=((1, ("Professor")),(2, ("Student"))),required=True)
	def clean(self, *args,**kwargs):
		username=self.cleaned_data.get("username")
		if username:
			user_qs = Product.objects.filter(username=username)
		if user_qs.count() != 0:
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