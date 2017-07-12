from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, View, CreateView
# Create your views here.

from menus.models import Item
from restaurants.models import RestaurantLocation

from .forms import RegisterForm
from .models import Profile

User = get_user_model()

class RegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'registration/register.html'
	success_url = '/'

	def dispatch(self, *args, **kwargs):
		# if self.request.user.is_authenticated():
			# return redirect("/login/")
		return super().dispatch(*args, **kwargs)

class ProfileFollowToggle(LoginRequiredMixin, View):
	def post(self, request, *args, **kwargs):
		# print(request.POST)
		user_to_toggle = request.POST.get("username").strip()
		profile_, is_following = Profile.objects.toggle_follow(request.user, user_to_toggle)
		print(is_following)
		# print(user_to_toggle)
		# print("amin")
		# print(user_to_toggle=="amin")
		# print(Profile.objects.all())
		# profile_ = Profile.objects.get(user__username=user_to_toggle)
		# # print(profile)
		# user = request.user
		# if user in profile_.followers.all():
		# 	profile_.followers.remove(user)
		# else:
		# 	profile_.followers.add(user)

		# # return redirect("/profiles/{}/".format(profile_.user.username))
		return redirect("/profiles/amin")

class ProfileDetailView(DetailView):
	template_name = 'profiles/user.html'

	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
			raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		print(context)
		# user = self.get_object()
		user = context['user']
		is_following = False
		if user.profile in self.request.user.is_following.all():
			is_following = True
		context['is_following'] = is_following

		query = self.request.GET.get('q')
		print(user)
		item_exists = Item.objects.filter(user=user).exists()
		qs = RestaurantLocation.objects.filter(owner=user)
		if query:
			qs = qs.search(query)
		if item_exists and qs.exists():
			context['locations'] = qs
		return context
