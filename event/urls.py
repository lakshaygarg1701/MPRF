from django.urls import path
from .views import Data, Details, subscribe

urlpatterns=[
	path('',Data.as_view(),name='list'),
	path("<int:pk>", Details.as_view(), name='detail'),
	path("notif/<int:pk>", subscribe.as_view(), name='post_new'),
]