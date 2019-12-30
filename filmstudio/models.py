from django.db import models

# Create your models here.


class filmstudio_lang(models.Model):
	lang = models.CharField(max_length=3, unique=True)
	header = models.CharField(max_length=999, blank=True)
	text = models.TextField(blank=True)
	table_field1 = models.CharField(max_length=999, blank=True)
	table_field2 = models.CharField(max_length=999, blank=True)
	table_field3 = models.CharField(max_length=999, blank=True)
	videos = models.CharField(max_length=999, blank=True)
	book = models.CharField(max_length=999, blank=True)
	def __str__(self):
		return self.lang

class filmstudio_img(models.Model):
	name = models.CharField("pildi nimi",max_length=999)
	img = models.ImageField(blank=True)
	def __str__(self):
		return self.name

class filmstudio_vid(models.Model):
	name = models.CharField("video nimi",max_length=999)
	url = models.CharField("video link",max_length=999)
	def __str__(self):
		return self.name

class filmstudio_inventory(models.Model):
	item = models.CharField(max_length=99, unique=True, blank=True)
	desc = models.CharField(max_length=999, blank=True)
	qty = models.CharField("mitu tk",max_length=2, blank=True)
	def __str__(self):
		return self.item