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

class subscribe(FormView):
	model=EventDetail
	form_class=SubscribeForm
	template_name="newsletter.html"


	def notif(request):
		if request.method == 'POST': # If the form has been submitted...
			print(request)
			form = SubscribeForm(request.POST) # A form bound to the POST data
			if form.is_valid(): # All validation rules pass
				post=form.save(commit=False)
				post.email=request.user
				post.save()
				return redirect('list')
			else:
				form= SubscribeForm() # An unbound form
				# EventDetail.objects.create()
		return render(request, 'newsletter.html', {'form': form,})