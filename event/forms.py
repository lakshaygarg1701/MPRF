from django import forms
from .models import EventDetail

class SubscribeForm(forms.ModelForm):
	id1=forms.IntegerField()#widget=forms.HiddenInput())
	email=forms.EmailField()#widget=forms.HiddenInput())

	class Meta:
		model = EventDetail
		fields = ("id1","email")

# from django import forms
# from .models import Page, Category

# class CategoryForm(forms.ModelForm):
#     name = forms.CharField(max_length=128, help_text="Please enter the category name.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

#     # An inline class to provide additional information on the form.
#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Category