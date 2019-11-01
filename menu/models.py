from django.db import models

# Create your models here.

class menu_lang(models.Model):
	header = models.CharField(max_length=999, blank=True)
	img = models.ImageField()

class menu_items(models.Model):
	item = models.CharField(max_length=99, unique=True)
	price = models.CharField(max_length=3, blank=True)
	def __str__(self):
		return self.item