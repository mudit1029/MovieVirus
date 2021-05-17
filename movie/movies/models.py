from django.db import models

# Create your models here.
class Movie(models.Model):
	#Creating choices for category field.
	Choices = (('B', 'Bollywood'),('H', 'Hollywood'),('A', 'Animated'),('S', 'South'))

	#Creating fields for the movie database.
	title = models.CharField(max_length=300)
	poster = models.CharField(max_length=300)
	imdbID = models.CharField(max_length=300)
	api = models.CharField(max_length=300)
	category = models.CharField(max_length=1, choices=Choices)
	dualAudio = models.BooleanField(default=False)
	languages = models.CharField(default="" , max_length=300)
	size = models.CharField(default="", max_length=300)
	screenshot1 = models.ImageField(upload_to = "uploads/" , default=0)
	screenshot2 = models.ImageField(upload_to = "uploads/" , default=0)
	screenshot3 = models.ImageField(upload_to = "uploads/" , default=0)
	screenshot4 = models.ImageField(upload_to = "uploads/" , default=0)
	google = models.CharField(max_length=300 , default="#")
	mega = models.CharField(max_length=300 , default="#")
	publish = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.title}"