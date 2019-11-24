from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm, UserLoginForm
from .models import Product, Course, Assignment, CourseList
from django.views.decorators.csrf import csrf_exempt
import os
import sqlite3
import csv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .forms import AssignmentForm
from .forms import CourseForm
from django.views.decorators.csrf import csrf_exempt
global cid
global Assignment_name
@csrf_exempt
def home_view(request, *args, **kwargs):
	return render(request, "home_page.html", {})
@csrf_exempt
def contact_view(request,*args, **kwargs):
	return render(request, "contact_page.html", {})
@csrf_exempt
def assignment_inst_view(request,*args, **kwargs):
	return render(request, "prof_assignmet_page.html", {})
@csrf_exempt
def course_inst_view(request,*args, **kwargs):
	return render(request, "course_prof_page.html", {})
@csrf_exempt
def assignment_stu_view(request,*args, **kwargs):
	return render(request, "assignment_student.html", {})
@csrf_exempt
def course_stu_view(request,*args, **kwargs):
    return render(request,"stu_home.html",{})
@csrf_exempt
def add_assign_view(request,*args, **kwargs):
    return render(request, "add_assign.html", {})
@csrf_exempt
def prof_home_view(request,*args, **kwargs):
    return render(request, "prof_home.html", {})
@csrf_exempt
def prof_create_course(request,*args, **kwargs):
    return render(request, "create_course.html", {})
@csrf_exempt
def upload_assign(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            reference = form.cleaned_data['references']
            data_entry(title,description,reference) # ****************************
            return HttpResponseRedirect('/is/course')
    else:
        form = AssignmentForm()
        return render(request, 'add_assign.html', {'form': form})
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        f=request.FILES['myfile']
        path="../../Submissions/"+f.name
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return HttpResponseRedirect('/st/course/assignment')
    else:
        form = UploadFileForm()
    return render(request, 'assignment_student.html', {'form': form})

@csrf_exempt
def prof_create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST or None)#, request.FILES or None)
        print(form)
        if form.is_valid():
            cname = form.cleaned_data['course_name']
            cid = form.cleaned_data['course_id']
            cyear = form.cleaned_data['year']
            course = CourseList(course_name = cname, course_id = cid,year = cyear)
            course.save()
            return HttpResponseRedirect('/is/course')
        #return HttpResponseRedirect('/is/course')
    else:
        form = CourseForm()
        return render(request, 'create_course.html', {'form': form})

@csrf_exempt
def prof_add_students(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        f=request.FILES['myfile']
        path="../../Submissions/"+f.name
        with open(path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        with open(path, 'r') as fle:
            for row in csv.reader(fle):
                course = Course(cid= cid,username = row)
@csrf_exempt
def index(request):
    return render(request, "home_page.html" , {})
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
            return redirect("home")
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
        k = Product.objects.filter(username=username)
        if k[0].category == 2:
            return render(request, 'stu_home.html' , {"username": username})
        else:
            return render(request, 'prof_home.html', {"username": username})
    return render(request, "products/products_validate.html", {"form":form, "title": title})
def register_view(request):
    return render(request, "form.html", {})
def logout_view(request):
    return render(request, "form.html", {})


# def main_view(request, *args, **kwargs):
# 	return render(request, "main_page.html", {})
