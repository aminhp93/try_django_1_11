from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse

from .utils import code_generator
# Create your models here.


User = settings.AUTH_USER_MODEL

class ProfileManager(models.Manager):
	def toggle_follow(self, request_user, username_to_toggle):
		profile_ = Profile.objects.get(user__username=username_to_toggle)
		user = request_user
		is_following = False
		if user in profile_.followers.all():
			profile_.followers.remove(user)
		else:
			profile_.followers.add(user)
			is_following = True
		return profile_, is_following

class Profile(models.Model):
	user 		= models.OneToOneField(User)
	followers 	= models.ManyToManyField(User, related_name='is_following', blank=True)
	# following 	= models.ManyToManyField(User, related_name='following', blank=True)
	activation_key = models.CharField(max_length=120, null=True, blank=True)
	activated	= models.BooleanField(default=False)
	timestamp	= models.DateTimeField(auto_now_add=True)
	update		= models.DateTimeField(auto_now=True)

	objects = ProfileManager()

	def __str__(self):
		return self.user.username

	def send_activation_email(self):
		print("activation")
		if not self.activated:
			self.activation_key = code_generator()
			self.save()
			path_ = reverse('activate', kwargs={"code": self.activation_key})
			subject = 'Activate Account'
			from_email = settings.DEFAULT_FROM_EMAIL
			message = 'Activate your account here: {}'.format(path_)
			recipient_list = [self.user.email]
			html_message = '<p>Activate your account here: {}</p>'.format(path_)
			print(html_message)
			# sent_mail = send_mail(
			# 		subject,
			# 		message,
			# 		from_email,
			# 		recipient_list,
			# 		fail_silently=False,
			# 		html_message=html_message
			# 	)
			sent_mail = False
			return sent_mail

def post_save_user_receiver(sender, instance, created, *wargs, **kwargs):
	if created:
		profile, is_created = Profile.objects.get_or_create(user=instance)
		default_user_profile = Profile.objects.get_or_create(user__id=1)[0]
		print(default_user_profile)
		print(default_user_profile.followers)
		default_user_profile.followers.add(instance)
		# default_user_profile.followers.remove(instance)

post_save.connect(post_save_user_receiver, sender=User)