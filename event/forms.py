from django import forms
from .models import EventDetail

class SubscribeForm(forms.ModelForm):
	id1=forms.IntegerField(widget=forms.HiddenInput())
	email=forms.EmailField(widget=forms.HiddenInput())

	class Meta:
		model = EventDetail
		fields = ("id1","email")