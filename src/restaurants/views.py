import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
	num = random.randint(0, 111111)
	template = "base.html"

	context = {"context_var": "True", "num": num}
	

	return render(request, template, context)