from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^calc/(?P<f_code>[\w-]+)/$', views.calc, name='calc'),
	url(r'^calc2/(?P<lat>.*)/(?P<lon>.*)/$', views.calc2, name='calc2'),
	url(r'^f_info/(?P<f_code>[\w-]+)/$', views.f_info, name='f_info'),
	url(r'^f_info2/(?P<lat>.*)/(?P<lon>.*)/$', views.f_info2, name='f_info2'),
]