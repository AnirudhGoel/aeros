from django.conf.urls import url

from . import views

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^calc/(?P<f_code>[\w-]+)/$', views.calc, name='calc'),
]