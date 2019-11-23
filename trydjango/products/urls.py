from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('course', views.login_view, name='stcourse')
]