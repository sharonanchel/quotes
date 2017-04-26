from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
    url(r'^quotes$',views.quotes),
    url(r'^users$',views.users),



]
