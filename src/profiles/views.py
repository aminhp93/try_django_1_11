from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
# Create your views here.

from menus.models import Item
from restaurants.models import RestaurantLocation

User = get_user_model()

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
		query = self.request.GET.get('q')
		print(user)
		item_exists = Item.objects.filter(user=user).exists()
		qs = RestaurantLocation.objects.filter(owner=user)
		if query:
			qs = qs.search(query)
		if item_exists and qs.exists():
			context['locations'] = qs
		return context
