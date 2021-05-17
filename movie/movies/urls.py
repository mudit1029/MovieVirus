from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
	path('', views.index , name="index"),
	path('movies/add/', views.add , name="add"),
	path('movies/<str:name>/', views.details , name="details"),
	path('movies/category/bollywood/', views.bolly , name="bolly"),
	path('movies/category/hollywood/', views.holly , name="holly"),	
	path('movies/category/hollywood/Dual-Audio/', views.hollyDual , name="hollyDual"),	
	path('movies/category/hollywood/Single-Audio/', views.hollySingle , name="hollySingle"),	
	path('movies/category/animated/', views.animated , name="animated"),	
	path('movies/category/animated/Dual-Audio/', views.animatedDual , name="animatedDual"),	
	path('movies/category/animated/Single-Audio/', views.animatedSingle , name="animatedSingle"),
	path('movies/category/south/', views.south , name="south"),
	path('?s=', views.search , name="search"),
]