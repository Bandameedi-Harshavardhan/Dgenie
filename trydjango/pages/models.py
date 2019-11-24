# Create your models here.
from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
	name		= models.TextField()
	username	= models.TextField()
	password	= models.TextField()
	category	= models.IntegerField(choices=((1, ("Professor")),
                                        (2, ("Student"))),
                                default=2)
class CourseList(models.Model):
	course_name = models.CharField(max_length=100)
	course_id = models.CharField(max_length=100)
	year = models.CharField(max_length=100)

class Course(models.Model):
	cid = models.TextField()
	username = models.ManyToManyField(Product,related_name = "user_course")

class Assignment(models.Model):
	title = models.CharField(max_length=100,unique=True)
	cid = models.ForeignKey(Course, on_delete=models.CASCADE)
	description = models.TextField()
	references = models.CharField(max_length=100)