from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('liuren', views.liuren, name='liuren'),
	path('chenyun', views.chenyun, name='chenyun'),
]
