from django.utils import timezone
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import FormView
from .models import Event, EventDetail
from django.http import HttpResponse, Http404, HttpResponseRedirect
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
		queryset = Event.objects.all()
		category = self.request.GET.get('category' or None)
		dept=self.request.GET.get('department' or None)

		if dept:
			queryset = queryset.filter(dept__iexact=dept)

		if category:
			if category=='Others':
				queryset=queryset.filter(category__iexact="")
			else:
				queryset = queryset.filter(category__iexact=category)

		queryset = queryset.order_by("date")
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

class subscribe(FormView):
	model=EventDetail
	form_class=SubscribeForm
	template_name="newsletter.html"


	def post(self,request,*args,**kwargs):
		pk=kwargs['pk']
		form = SubscribeForm(request.POST or None) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			form.save()
			return redirect('/content',permanent=True)
		return render(self.request, 'newsletter.html', {'form': form})