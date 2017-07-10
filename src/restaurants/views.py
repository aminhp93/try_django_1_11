import random

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


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