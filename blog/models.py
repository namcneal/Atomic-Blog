from django.db import models

# Create your models here.


STATUS = (
	(0, "draft"),
	(1, "publish")
)

class Article(models.Model):
	slug       = models.SlugField(max_length=200, unique=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)
	status     = models.IntegerField(choices=STATUS, default=0)

	field      = models.CharField(max_length=20, default="") # Values: phys, math, prog
	title      = models.CharField(max_length=200, unique=True)
	subtitle   = models.CharField(max_length=400, unique=False)

	class Meta:
		ordering = ['created_on']

	def __str__(self):
		return self.title