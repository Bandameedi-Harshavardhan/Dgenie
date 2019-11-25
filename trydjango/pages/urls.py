from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.home_view, name='home'),
	path('contact', views.contact_view, name='contact'),
	# path('main', views.main_view, name='main'),
	path('is/assignment', views.assignment_inst_view, name='IA'),
	#path('is/course', views.course_inst_view, name='IC'),
	#path('st/course/assignment', views.assignment_stu_view, name='SA'),
	#path('upload', views.upload_file, name='UF'),
	#url(r'^upload/(?P<title>[-\w\s]+)/(?P<name>[-\w\s]+)/$', views.upload_file, name='UF'),
	path('st/course', views.course_stu_view, name = 'SC'),
	url(r'^is/new/(?P<title>[-\w\s]+)/$', views.add_assign_view, name='AA'),
	path('phome', views.prof_home_view, name='phome'),
	path('createc', views.prof_create_course, name = 'ccreate'),
	url(r'^is/add_stu/(?P<title>[-\w\s]+)/$', views.add_stu ,name = 'ASTU'),
	url(r'^st/course/(?P<title>[-\w\s]+)/$', views.course_stu_view, name='student course'),
	url(r'^st/assignment/(?P<title>[-\w\s]+)/$', views.assignment_stu_view, name='student assignment'),
	url(r'^is/course/(?P<title>[-\w\s]+)/$', views.course_prof_view, name='prof course'),
	url(r'^is/assignment/(?P<title>[-\w\s]+)/$', views.assignment_inst_view, name='prof assignment'),
	url(r'^is/add_ins/(?P<title>[-\w\s]+)/$', views.add_ins ,name = 'AINS')

	# path('is/course/add_ins', views.add_ins , name = 'AINS')
]