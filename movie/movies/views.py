from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

#Importing Movie model from models file. 
from .models import Movie
# Create your views here.

# Index page view.
def index(request):

	#Get all the movies from the database excluding the movies which are not published yet in descending oreder by id column.
	movies = Movie.objects.all().exclude(publish=False).order_by('-id')
	
	#Get the current login user and access the username value. 
	user = request.user.username
	
	#Return the index page with the below key value pairs. 
	return render(request, "movies/index.html", {
			"movies": movies,
			"user": user.capitalize(),
			})

# Search Bar view.
def search(request):

	#Get the current login user and access the username value.
	user = request.user.username
	
	#When the search query entered run this:
	if request.method == "GET":

		# Get what the user typed in the search bar.
		title = request.GET["s"]

		#Access database and search for the user query and get the movie in the movies variable.
		movies = Movie.objects.all().filter(title__contains=title).exclude(publish=False)

		#Return the index page with the below key value pairs. 
		return render(request, "movies/index.html", {
			"movies": movies,
			"user": user.capitalize(),
			})				

# Add Movies View.
def add(request):
	
	#Get the current login user and access the username value.
	user = request.user.username

	if not request.user.is_superuser :
		return HttpResponseRedirect(reverse("movies:index")) 

	# When the admin clicks on "Add to database" button run this. 
	if request.method == "POST":

		#get all the input fields value.
		imdb = request.POST["imdbid"]
		title = request.POST["title"]
		image = request.POST["image"]
		token = request.POST["api"]

		#Add the movie details into the database with the above data.
		add = Movie(title=title , poster=image , imdbID=imdb , api=token)

		#Save the movie into the database.
		add.save()

		#return add page with the Successful Message.
		return render(request, "movies/add.html", {
			"message": "Entry Added To Database",
			"user": user.capitalize()
			})

	# When the user gets on add route open add page with the user credentials.	
	return render(request, "movies/add.html", {
		"user": user.capitalize()
		})	

# Movie Details Page view
def details(request , name):

	#Get the current login user and access the username value.
	user = request.user.username

	# get the movie from the database whose title is stored the name parameter.
	movie = Movie.objects.get(title=name)

	# Return the movie data in details page by key value pair.
	return render(request, "movies/details.html", {
		"movie": movie,
		"user": user.capitalize()
		})	

# Bollywood Movies Page View.
def bolly(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "B" or "Bollywood" in descending order.
	movies = Movie.objects.all().filter(category="B").order_by('-id')

	#return Index page with the bollywood movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})	

# Hollywood Movies Page View.
def holly(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "H" or "Hollywood" in descending order.
	movies = Movie.objects.all().filter(category="H").order_by('-id')

	#return Index page with the hollywood movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})

# Hollywood (Dual - Audio) Movies Page View.
def hollyDual(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "H" or "Hollywood" and DualAudio = True in descending order.
	movies = Movie.objects.all().filter(category="H" , dualAudio = True).order_by('-id')

	#return Index page with the dual audio hollywood movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})

# Hollywood (Single - Audio) Movies Page View.
def hollySingle(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "H" or "Hollywood" and DualAudio = False in descending order.
	movies = Movie.objects.all().filter(category="H" , dualAudio = False).order_by('-id')

	#return Index page with the single audio hollywood movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})						

# Animated Movies Page View.
def animated(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "A" or "Animated"in descending order.
	movies = Movie.objects.all().filter(category="A").order_by('-id')

	#return Index page with the animated movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})

# Animated (Dual - Audio) Movies Page View.
def animatedDual(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "A" or "Animated" and DualAudio = True in descending order.
	movies = Movie.objects.all().filter(category="A" , dualAudio = True).order_by('-id')

	#return Index page with the dual audio animated movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})

# Animated (Single - Audio) Movies Page View.
def animatedSingle(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "A" or "Animated" and DualAudio = False in descending order.
	movies = Movie.objects.all().filter(category="A" , dualAudio = False).order_by('-id')

	#return Index page with the single audio animated movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})	

# South Movies Page View.
def south(request):

	#Get the current login user and access the username value.
	user = request.user.username

	#Access database and get all the movies whose category value is "S" or "South" in descending order.
	movies = Movie.objects.all().filter(category="S").order_by('-id')

	#return Index page with the south movies.
	return render(request, "movies/index.html", {
		"movies": movies,
		"user": user.capitalize()
		})								