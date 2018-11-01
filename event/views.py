from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Event, EventDetail
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from .forms import SubscribeForm
from datetime import datetime

# Create your views here.
class Data(ListView):
	model=Event
	template_name="list1.html"
	
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context
	
	def get_queryset(self):
		now=timezone.now()
		print(now)
		queryset = Event.objects.all()
		category = self.request.GET.get('category' or None)
		dept=self.request.GET.get('department' or None)
		
		print (category,dept)
		if dept:
			queryset = Event.objects.filter(dept__iexact=dept)
		
		if category:
			queryset = Event.objects.filter(category__iexact=category)

		queryset = queryset.order_by("id1")
		return queryset;

class Details(DetailView):
	model=Event
	template_name="detail.html"

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		pk=self.kwargs['pk']
		obj = get_object_or_404(Event,pk=pk)
		print(context)
		return context

class subscribe(TemplateView):
	model=EventDetail
	template_name="detail.html"