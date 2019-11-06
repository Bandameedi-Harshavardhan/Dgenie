from django.shortcuts import render
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the Products index.")
def Product_Create_View(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save
	context = {
		'form' : form
	}
	return render(request, "products/products_create.html", context)