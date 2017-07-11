from django.conf import settings
from django.db import models

from restaurants.models import RestaurantLocation

# Create your models here.
class Item(models.Model):
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	restaurant 	= models.ForeignKey(RestaurantLocation)
	name 		= models.CharField(max_length=120)
	content 	= models.TextField(help_text='separete each item by comma')
	exclude 	= models.TextField(blank=True, null=True, help_text='separete each item by comma')
	public 		= models.BooleanField(default=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated		= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['updated', '-timestamp']

	def __str__(self):
		return self.name

	def get_content(self):
		return self.content.split(",")

	def get_exclude(self):
		return self.exclude.split(",")

