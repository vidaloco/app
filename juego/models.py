from django.db import models

# Create your models here.

class Juego(object):
	nombre = models.CharField(max_length = 45, primary_key = True)
	genero = models.CharField(max_length = 45)
	compania = models.CharField(max_length = 45)
	portada = models.ImageField(upload_to = 'static')
	precio = models.CharField(max_length = 45)

	def __init__(self):
		return self.nombreJuego