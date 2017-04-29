from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index')
	url(r'^calc/(?P<userId>[0-9]+)/', views.calc, name='calc'),
]