from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
	template = ""

	context = {}
	return HttpResponse("Hello workd")

	# return render(request, template, context)