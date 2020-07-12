from django.db import models

# Create your models here.
from blog.models import Category


class ProjectCategory(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return str(self.name)

	def __repr__(self):
		return  str(self.name)

class Project(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=100, null=True)
	description = models.TextField()
	technology = models.CharField(max_length=100)
	# image = models.FilePathFioeld(path="/img")
	image = models.ImageField(upload_to='img',null=True)
	category = models.ForeignKey(ProjectCategory,on_delete=models.PROTECT)

	def __str__(self):
		return str(self.title)

	def __repr__(self):
		return '{}'.format(self.category)


