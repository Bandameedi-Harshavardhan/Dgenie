from django.urls import path

from . import views

urlpatterns = [
	path('', views.home_view, name='home'),
	path('contact', views.contact_view, name='contact'),
	# path('main', views.main_view, name='main'),
	path('is/assignment', views.assignment_inst_view, name='IA'),
	path('is/course', views.course_inst_view, name='IC'),
	path('st/assignment', views.assignment_stu_view, name='SA'),
	path('upload', views.upload_file, name='UF')
]