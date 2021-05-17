from django.contrib import admin

# Importing Movie Model From Models File.
from .models import Movie

# Register your models here.
class display(admin.ModelAdmin):
	list_display = ("title" , "poster" , "imdbID" , "api" , "publish")

# Registering movie Model In admin Site whose display is according to the above class.
admin.site.register(Movie, display)