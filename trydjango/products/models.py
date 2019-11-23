from django.db import models

# Create your models here.
class Product(models.Model):
	name		= models.TextField()
	username	= models.TextField()
	password	= models.TextField()
	category	= models.IntegerField(choices=((1, ("Professor")),
                                        (2, ("Student"))),
                                default=2)