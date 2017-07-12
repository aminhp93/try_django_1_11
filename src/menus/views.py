from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View

# Create your views here.
from .forms import ItemForm
from .models import Item

class HomeView(View):
	def get(sef, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "home.html", {})

		user = request.user
		is_following_user_ids = [x.user.id for x in user.is_following.all()]
		qs = Item.objects.filter(user__id__in=is_following_user_ids, public=True).order_by("-updated")[:3]
		print(qs)

		return render(request, "menus/home-feed.html", {"object_list": qs})

class ItemListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemCreateView(LoginRequiredMixin, CreateView):
	template_name = 'form.html'
	form_class = ItemForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super().form_valid(form)

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['user'] = self.request.user
		kwargs['instance'] = Item.objects.filter(user=self.request.user).first()
		return kwargs

	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["title"] = "Create Item"
		return context		

class ItemDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)

class ItemUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'menus/detail-update.html'
	form_class = ItemForm
	def get_queryset(self):
		print("Tes")
		return Item.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args,**kwargs)
		context["title"] = "Update Item"
		return context

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs
