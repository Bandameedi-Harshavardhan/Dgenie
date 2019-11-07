import os
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponseRedirect
from .forms import UploadFileForm

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
def upload_file(request):
    print("nayan is debugging")
    global Course_name
    global Assignment_name
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print("nayan is debugging inside")
        if form.is_valid():
            print("nayan is debugging little inside")
        handle_uploaded_file(request.FILES['myfile'])
        print("nayan is debugging deep inside")
        return HttpResponseRedirect('/st/assignment')
    else:
        form = UploadFileForm()
    return render(request, 'assignment_student.html', {'form': form})

def handle_uploaded_file(f):
    print("nayan is debugging handle")
    path="../../Submissions/"+f.name
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
# def main_view(request, *args, **kwargs):
# 	return render(request, "main_page.html", {})
