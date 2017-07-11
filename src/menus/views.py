from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

# Create your views here.
from .forms import ItemForm
from .models import Item

class ItemListView(ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemCreateView(CreateView):
	template_name = 'form.html'
	form_class = ItemForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super().form_valid(form)

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["title"] = "Create Item"
		return context		

class ItemDetailView(DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemUpdateView(UpdateView):
	template_name = 'form.html'
	form_class = ItemForm
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["title"] = "Update Item"
		return context