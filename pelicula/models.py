from django.db import models

# Create your models here.
class Pelicula(object):
	nombre = models.CharField(max_length = 45)
	portada = models.ImageField(upload_to = 'static')
	precio = models.CharField(max_length = 45)
	

	def __init__(self):
		return self.nombrePelicula
		