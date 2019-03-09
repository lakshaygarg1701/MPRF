from django.urls import path
from .views import Data, Details, subscribe, Add

urlpatterns=[
	path('',Data.as_view(),name='list'),
	path("<int:pk>", Details.as_view(), name='detail'),
	path("notif/<int:pk>", subscribe.as_view(success_url='/<int:pk>'), name='post_new'),
	path("add/form",Add.as_view())
]