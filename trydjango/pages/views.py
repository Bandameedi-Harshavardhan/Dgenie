from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home_page.html", {})
def contact_view(request,*args, **kwargs):
	return render(request, "contact_page.html", {})