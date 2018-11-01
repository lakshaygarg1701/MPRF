from django import forms
from .models import EventDetail

class SubscribeForm(forms.Form):
	id1=forms.IntegerField()
	emailid=forms.CharField(max_length=200)

	class Meta:
		model = EventDetail
		fields = ("id1","emailid")