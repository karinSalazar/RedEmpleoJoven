from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def str(self):
        return self.name + ": " + str(self.videofile)


class Colaborador(models.Model):
	nombreColaborador = models.CharField(max_length=40)
	link = models.URLField(max_length=500,null=True)
	logo = models.ImageField(upload_to ='ColaboradorL/',null=True)
	foto = models.ImageField(upload_to ='ColaboradorF/',null=True)
	mision = models.CharField(max_length=400,blank=True,null=True)
	fecha = models.DateField(null=True)
	
	class Meta:
		verbose_name = 'Colaborador'
		verbose_name_plural = 'Colaboradores'

	def __str__(self):
		return str(self.nombreColaborador)

class Proyecto(models.Model):
	order = models.IntegerField(blank=True, null=True)
	nombreProyecto = models.CharField(max_length=40,null=True)
	descripcion = models.CharField(max_length=300,null=True)
	imagen = models.ImageField(upload_to ='proyecto/', null = True)
	
	class Meta:
		verbose_name = 'Proyecto'
		verbose_name_plural = 'Proyectos'
		ordering = ['order']

	def __str__(self):
		return str(self.nombreProyecto)



class Noticia(models.Model):
	fecha = models.DateField(blank=True, null=True)
	link = models.URLField(max_length=500)
	titulo = models.CharField(max_length=100,blank=True, null=True)
	descripcion = models.CharField(max_length=300,blank=True, null=True)
	imagen = models.ImageField(upload_to = 'noticia/', default = 'pic_folder/None/partner-3.png')
	order = models.IntegerField(blank=True, null=True)
	body = models.TextField(blank=True, null=True)
		
	class Meta:
		verbose_name = 'Noticia'
		verbose_name_plural = 'Noticias'
		ordering = ["-fecha"] 

	def __str__(self):
		return str(self.order) + " " + str(self.titulo)+ " " + str(self.descripcion) 


class Recurso(models.Model):
	nombreRecurso = models.CharField(max_length=40)
	archivo = models.FileField(null=True,upload_to='transferencias/')
	link = models.URLField(null=True, blank=True)
	proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
	imagen = models.ImageField(upload_to ='recursos/', null = True)


	class Meta:
		verbose_name = 'Recurso'
		verbose_name_plural = 'Recursos'

	def __str__(self):
		return str(self.nombreRecurso)


