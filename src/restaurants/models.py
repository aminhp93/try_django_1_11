from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL

# Create your models here.

class RestaurantLocationQuerySet(models.query.QuerySet):
	def search(self, query):
		return self.filter(
			Q(name__icontains=query)|
			Q(location__icontains=query)|
			Q(category__icontains=query)|
			Q(item__name__icontains=query)|
			Q(item__content__icontains=query)|
			Q(item__exclude__icontains=query)
		)

class RestaurantLocationManager(models.Manager):
	def get_queryset(self):
		return RestaurantLocationQuerySet(self.model, using=self._db)

	def search(self, query):
		return self.get_queryset().search(query)

class RestaurantLocation(models.Model):
	owner 		= models.ForeignKey(User)
	name 		= models.CharField(max_length=120)
	location 	= models.CharField(max_length=120, null=True, blank=True)
	category 	= models.CharField(max_length=120, null=True, blank=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)
	updated 	= models.DateTimeField(auto_now=True)
	slug		= models.SlugField(null=True, blank=True)

	objects = RestaurantLocationManager()
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("restaurants:detail", kwargs={"slug": self.slug})

	@property
	def title(self):
		return self.name
	
def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	print("saving")
	print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
	
# def rl_post_save_receiver(sender, instance, created, *args, **kwargs):
# 	print("saved")
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)