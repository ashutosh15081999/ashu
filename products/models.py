from django.db import models

# Create your models here.

class Product(models.Model):
	title       = models.CharField(max_length = 120)
	description = models.TextField(blank = True,null = False)
	price       = models.DecimalField(decimal_places=2, max_digits=1000)
	summary     = models.TextField(default='are you good!', null=False)
	feedback    = models.BooleanField(default = False)