from django.db import models

# Create your models here.

class Otro(object):
	nombre = models.CharField(max_length = 45, primary_key = True)
	foto = models.ImageField(upload_to = 'static')
	precio = models.CharField(max_length = 45)

	def __init__(self):
		return self.nombreProductos