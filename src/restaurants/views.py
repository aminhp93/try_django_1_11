import random

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation


# Create your views here.
def home(request):
	num = random.randint(0, 111111)
	lists = [2, 5, 6]

	template = "home.html"
	context = {
			"context_var": "True",
			"num": num, 
			"bool_item": True,
			"lists": lists
	}

	return render(request, template, context)

def contact(request):
	template = "contact.html"
	context = {
			"title": "Contact"
	}

	return render(request, template, context)

def about(request):
	template = "about.html"
	context = {
			"title": "About"
	}

	return render(request, template, context)

class ContactView(View):
	def get(self, request, *args, **kwargs):
		template = "contact.html"
		context = {}
		return render(request, template, context)

class HomeTemplateView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		num = random.randint(0, 111111)
		lists = [2, 5, 6]

		context = {
				"context_var": "True",
				"num": num, 
				"bool_item": True,
				"lists": lists
		}
		return context

class AboutTemplateView(TemplateView):
	template_name = "about.html"


class ContactTemplateView(TemplateView):
	template_name = "contact.html"


def restaurant_listview(request):
	queryset = RestaurantLocation.objects.all()
	template_name = 'restaurants/restaurants_list.html'
	context = {	
		"object_list": queryset,
	}
	return render(request, template_name, context)

class RestaurantListView(ListView):
	template_name = 'restaurants/restaurants_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset = RestaurantLocation.objects.filter(
					Q(category__iexact=slug) | 
					Q(category__icontains=slug)

				)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset

class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		return context

	def get_object(self, *args, **kwargs):
		rest_id = self.kwargs.get("rest_id")
		obj = get_object_or_404(RestaurantLocation, id=rest_id)
		return obj


