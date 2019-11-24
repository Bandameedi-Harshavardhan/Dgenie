from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Product(models.Model):
	name		= models.TextField()
	username	= models.TextField()
	password	= models.TextField()
	category	= models.IntegerField(choices=((1, ("Professor")),
                                        (2, ("Student"))),
                                default=2)
	# cgiven		= models.ListCharField(models.CharField(max_length=10, blank=True), blank = True)
	# ctaken		= models.ListCharField(models.CharField(max_length=10, blank=True), blank = True)