from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm, UserLoginForm
from .models import Product
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
	return HttpResponse("Hello, world. You're at the Products index.")
@csrf_exempt
def product_view(request):
	context = {
		'name': obj.Name,
		'username': obj.Username
	}
	return render(request, "products/detail.html",context)
@csrf_exempt
def Product_Create_View(request):
	my_form = ProductForm()
	if request.method == "POST":
		my_form = ProductForm(request.POST)
		if my_form.is_valid():
			Product.objects.create(**my_form.cleaned_data)
			my_form = ProductForm()
	context={
		"form" : my_form
	}
	return render(request, "products/products_create.html", context)
@csrf_exempt
def login_view(request):
	title="Login"
	form =UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		form = UserLoginForm()
		return render(request, 'stu_home.html' , {"username": username})
	return render(request, "products/products_validate.html", {"form":form, "title": title})
def register_view(request):
	return render(request, "form.html", {})
def logout_view(request):
	return render(request, "form.html", {})