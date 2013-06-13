from django.db import models

class Alumnos(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=30)
	edad = models.IntegerField(max_length=10)

	def __unicode__(self):
		return self.apellido

	class Meta:
		verbose_name_plural=u'Alumnos'