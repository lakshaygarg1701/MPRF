from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Event
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404

# Create your views here.
class Data(ListView):
	model=Event
	template_name="list1.html"
	
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		return context
	
	def get_queryset(self):
		queryset=Event.objects.all()
		return queryset

class Details(DetailView):
	model=Event
	template_name="detail.html"

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		pk=self.kwargs['pk']
		# pk=20
		# print('???',pk)
		obj = get_object_or_404(Event,pk=pk)
		print(context)
        # if not obj.publish:
        # 	raise Http404
        # print(obj)
        # print(context)
		return context