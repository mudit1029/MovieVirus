from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
	path('', views.index , name="index"),
	path('login/', views.signIn , name="login"),
	path('logout/', views.signOut , name="logout"),
	path('register/', views.register , name="register"),
	path('forgot/', views.forgot , name="forgot"),
	path('edit/', views.edit  ,name="edit"),
]