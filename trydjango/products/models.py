from django.db import models

# Create your models here.
class Product(models.Model):
	name		= models.TextField()
	username	= models.TextField()
	password	= models.TextField()
	category	= models.TextField()