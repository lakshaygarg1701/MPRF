from django.urls import path
from .views import Data, Details, subscribe

urlpatterns=[
	path('',Data.as_view(),name='list'),
	path("<int:pk>", Details.as_view(), name='detail'),
	# path("<int:pk>/newsletter/",subscribe.as_view(success_url='/content')),
	path('post/new', subscribe.as_view(success_url='/content'), name='post_new'),
]