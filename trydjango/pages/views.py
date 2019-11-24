import os
import sqlite3
import csv
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .forms import AssignmentForm
from .forms import CourseForm
from django.views.decorators.csrf import csrf_exempt
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
            data_entry(title,description,reference)
            print(title) #Add assignment to the database.
            print(description)
            print(reference)
            return HttpResponseRedirect('/is/course')
    else:
        form = AssignmentForm()
        return render(request, 'add_assign.html', {'form': form})
@csrf_exempt
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
@csrf_exempt
def handle_uploaded_file(f):
    path="../../Submissions/"+f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
@csrf_exempt
def data_entry(title,description,reference):
    connec = sqlite3.connect('db.sqlite3')
    bla = connec.cursor()
    bla.execute('CREATE TABLE IF NOT EXISTS uspw(Title text,Description text,reference text) ')
    bla.execute("INSERT INTO uspw (Title,Description,reference) VALUES(?,?,?)", (title, description, reference))
    connec.commit()
    connec.close()
@csrf_exempt
def prof_create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST or None)#, request.FILES or None)
        print(form)
        if form.is_valid():
            cname = form.cleaned_data['course_name']
            cid = form.cleaned_data['course_id']
            cyear = form.cleaned_data['year']
            connec = sqlite3.connect('db.sqlite3')
            bla = connec.cursor()
            command = 'CREATE TABLE IF NOT EXISTS Course (CID text,username text)'
            bla.execute(command)
            student_list = request.FILES['student_list']
            path="../../Submissions/"+student_list.name
            with open(path, 'wb+') as destination:
                for chunk in student_list.chunks():
                    destination.write(chunk)
            # prof_list = request.FILES['prof_list']
            with open(path , 'r') as fin:
                for row in csv.reader(fin):
                    bla.execute("INSERT INTO Course(CID ,username) VALUES(?,?);", (cid,row))
            # with open(prof_list , 'r') as fin:
            #     for row in csv.reader(fin):
            #         bla.execute("INSERT INTO Course(CID ,username) VALUES(?,?);", (cid,row))            
            connec.commit()
            connec.close()

            return HttpResponseRedirect('/is/course')
        return HttpResponseRedirect('/is/course')
    else:
        form = CourseForm()
        return render(request, 'create_course.html', {'form': form})



# def main_view(request, *args, **kwargs):
# 	return render(request, "main_page.html", {})
