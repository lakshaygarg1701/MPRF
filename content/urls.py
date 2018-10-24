from django.urls import path
from .views import Data, Details

urlpatterns=[
	path('',Data.as_view(),name='list'),
	path("<int:pk>", Details.as_view()),
]