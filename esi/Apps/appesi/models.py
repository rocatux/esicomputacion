from __future__ import unicode_literals
from django.db import models
# Create your models here.


class Tipopagomod(models.Model):
	tipo = models.CharField(max_length=300,default="")

	def __str__(self):
		return self.tipo

class Tipocursomod(models.Model):
	nombre = models.CharField(max_length=50,default="")

	def __str__(self):
		return self.nombre

class Cursomod(models.Model):
	fechainicio = models.DateField()
	fechafinal = models.DateField()
	horarioini = models.TimeField()
	horariofin = models.TimeField()
	dias = models.CharField(max_length=500,default="")
	requisitos = models.CharField(max_length=1000,default="")
	descripcion = models.CharField(max_length=1000,default="")
	objetivos = models.CharField(max_length=1000,default="")
	dirigido =  models.CharField(max_length=1000,default="")
	costo = models.CharField(max_length=15,default="")
	costototal = models.CharField(max_length=15,default="")
	tipocursof = models.ForeignKey(Tipocursomod,default="")
	tipopagof = models.ForeignKey(Tipopagomod,default="")

	def __str__(self):
		return self.descripcion

