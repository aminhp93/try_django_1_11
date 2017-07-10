import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
	num = random.randint(0, 111111)
	lists = [2, 5, 6]
	template = "base.html"

	context = {
			"context_var": "True",
			"num": num, 
			"bool_item": True,
			"lists": lists
	}

	return render(request, template, context)