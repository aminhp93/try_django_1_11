from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

# Create your models here.


User = settings.AUTH_USER_MODEL

class Profile(models.Model):
	user 		= models.OneToOneField(User)
	followers 	= models.ManyToManyField(User, related_name='is_following', blank=True)
	# following 	= models.ManyToManyField(User, related_name='following', blank=True)
	activated	= models.BooleanField(default=False)
	timestamp	= models.DateTimeField(auto_now_add=True)
	update		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.user.username

def post_save_user_receiver(sender, instance, created, *wargs, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(user=instance)
		default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
		print(default_user_profile)
		print(default_user_profile.followers)
		default_user_profile.followers.add(instance)
		# default_user_profile.followers.remove(instance)

post_save.connect(post_save_user_receiver, sender=User)