from django import forms
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
	file = forms.FileField()