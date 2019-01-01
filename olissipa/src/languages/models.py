from django.db import models


class Person(models.Model):
	name = models.CharField(max_length=120)
	language = models.CharField(max_length=120)

	def __str__(self):
		return self.name


