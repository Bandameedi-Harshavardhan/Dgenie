import os
import sqlite3
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .forms import AssignmentForm

def home_view(request, *args, **kwargs):
	return render(request, "home_page.html", {})
def contact_view(request,*args, **kwargs):
	return render(request, "contact_page.html", {})
def assignment_inst_view(request,*args, **kwargs):
	return render(request, "prof_assignmet_page.html", {})
def course_inst_view(request,*args, **kwargs):
	return render(request, "course_prof_page.html", {})
def assignment_stu_view(request,*args, **kwargs):
	return render(request, "assignment_student.html", {})
def course_stu_view(request,*args, **kwargs):
    return render(request,"stu_home.html",{})
def add_assign_view(request,*args, **kwargs):
    return render(request, "add_assign.html", {})
def upload_assign(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            reference = form.cleaned_data['references']
            data_entry(title,description,reference)
            print(title) #Add assignment to the database.
            print(description)
            print(reference)
            return HttpResponseRedirect('/is/course')
    else:
        form = AssignmentForm()
        return render(request, 'add_assign.html', {'form': form})

def upload_file(request):
    global Course_name
    global Assignment_name
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
        handle_uploaded_file(request.FILES['myfile'])
        return HttpResponseRedirect('/st/course/assignment')
    else:
        form = UploadFileForm()
    return render(request, 'assignment_student.html', {'form': form})

def handle_uploaded_file(f):
    path="../../Submissions/"+f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def data_entry(title,description,reference):
    connec = sqlite3.connect('db.sqlite3')
    bla = connec.cursor()
    bla.execute('CREATE TABLE IF NOT EXISTS uspw(Title text,Description text,reference text) ')
    bla.execute("INSERT INTO uspw (Title,Description,reference) VALUES(?,?,?)", (title, description, reference))
    connec.commit()
    connec.close()
# def main_view(request, *args, **kwargs):
# 	return render(request, "main_page.html", {})
