from django.shortcuts import render

#Import all the forms from the form file
from .forms import *

#Import Redirect and response function
from django.http import HttpResponseRedirect , HttpResponse

#Reversing or redirecting the user.
from django.urls import reverse

#Importing authentication functions for the user
from django.contrib.auth import authenticate , login , logout

#Import CustomUser Model from teh models file
from .models import CustomUser

#Import send_mail function for sending email to user
from django.core.mail import send_mail

#When user already exist in register view.
from django.db import IntegrityError

#When sending email gets an error.
import socket

#Generates random number
import random

# Create your views here.

# Creating Index Page View.
def index(request):

	# If the user is not logged in redirect the user to login page.
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("users:login"))

	# If user is looged in open index page.	
	return render(request, "users/index.html")

# Creating Index Page View.
def signIn(request):

	# If user is looged in redirect to index page.
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("users:index"))

	# When form is submitted by the user run this.	
	if request.method == "POST":

		#Get all the data posted by the user and store the data in form variable.
		form = LoginForm(request.POST)

		# If form does'nt contain any problems run this.
		if form.is_valid():

			#Get the username and password from the submitted form.
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]

			#Set the username field to the user provided username.
			kwargs = {'username':username}	

			#If the username field contains an "@" in it then set the email field to the user provided username.
			if '@' in username:
				kwargs = {'email':username}

			# try to get the user by the user data.	
			try :	
				user = CustomUser.objects.get(**kwargs)

			# if the user does not exist in the database	
			except CustomUser.DoesNotExist:

				# Return the login page again with the provided data and with a message says "User Does Not Exist".
				return render(request, "users/login.html",{
					"message": "User Does Not Exist",
					"form": form
					})

			# If the user activity status is false			
			if user.is_active == False :

				#return the register page With the below message and with an registeration form.
				return render(request, "users/register.html",{
					"message": "Account Error : Re-Register with the same credentials.",
					"form": RegisterForm(),
					"button": "Register"
					})	

			# If the user provided password match the user password in the database					
			if user.check_password(password):

				# Grant login to the user
				login(request, user)

			# Otherwise if the password did'nt match	
			else :

				#Return login page again with a message "Invalid Credentials"
				return render(request, "users/login.html",{
				"message": "Invalid Credentials",
				"form": form
				})

			# When user set to login return the user to the index page of movies app.		
			return HttpResponseRedirect(reverse("movies:index"))

	# Open login page when the user method = GET.			
	return render(request, "users/login.html", {
		"form": LoginForm()
		})	

# Creating edit page view.
def edit(request):

	# if user is not logged in redirect the user to the login page.
	if not request.user.is_authenticated:
		return render(request, "users/login.html", {
		"form": LoginForm()
		})

	# if user submits the data in it	
	if request.method == "POST":

		# get all the data provided by the user
		fname = request.POST["fname"]	
		lname = request.POST["lname"]	
		number = request.POST["number"]	

		# Convert the number into an string.
		number = str(number)

		# If the text fields is empty return edit page again with the provided data and with the below message.
		if len(fname) == 0 or len(lname) == 0 :
			return render(request, "users/edit.html", {
				"fname": fname,
				"lname": lname,
				"number": number,
				"message": "Input Fields Cannot Be Empty" 
			})

		# If the number contains 10 digits	
		if len(number) == 10 :

			# get the current logged in user
			user = request.user

			# set the user's firstname , lastname and number
			user.first_name = fname
			user.last_name = lname
			user.number = number

			# save the user with the new details.
			user.save()

			# return the user to the index page.
			return HttpResponseRedirect(reverse("users:index"))

		# if the number does not contains 10 digits return edit page again with the provided data and with a message "Number Field must include 10 digits".	
		return render(request, "users/edit.html", {
			"fname": fname,
			"lname": lname,
			"number": number,
			"message": "Number must be of 10 digits." 
		})

	# if user's request method = GET get the current logged in user with their data	
	user = request.user
	fname = user.first_name
	lname = user.last_name
	number = user.number

	# open edit page with the user data.
	return render(request, "users/edit.html", {
		"fname": fname,
		"lname": lname,
		"number": number
		})

#Creating signOut view.
def signOut(request):

	#Sends an request to logout the user.
	logout(request)

	#when successfully logged out redirect the user to the inedx page of movies app.
	return HttpResponseRedirect(reverse("movies:index"))	

# Creating Register View.
def register(request):

	#If user is already logged in redirect the user to the index page.
	if request.user.is_authenticated :
		return HttpResponseRedirect(reverse("users:index"))

	# If the user submits the form	
	if request.method == "POST":

		#Store all the user provided data in the form variable.
		form = RegisterForm(request.POST)

		#If form is valid to process
		if form.is_valid():

			#fetch all the user provided data
			username = form.cleaned_data["username"]
			email = form.cleaned_data["email"]
			password = form.cleaned_data["password"]
			confirm = form.cleaned_data["confirm"]

			#if password is not = confirm password
			if password != confirm:

				#return the user to register page with the below message and the provided data.
				return render(request, "users/register.html", {
					"message": "Both Password Should Match",
					"form": form,
					"button": "Register",
					"login": "Back"
					})

			#if password and confirm matched , try to get the user from the database with the user provided username.	
			try :
				user = CustomUser.objects.get(username=username)

			# if the user is not in the database	
			except CustomUser.DoesNotExist :

				#try to get the user with the user provided email
				try :
					user = CustomUser.objects.get(email=email)

				# if their is no user	
				except CustomUser.DoesNotExist :

					# Create the user with the user provided data
					user = CustomUser.objects.create_user(username,email,password)

					# create a random 6 digit no. and save it to otp variable.
					otp = random.randint(100000 , 999999)

					# save the otp in the newly created user otp field
					user.otp = otp

					#set the user activity status to false
					user.is_active = False

					#save the user in the database.
					user.save()

					#Create the body of an email which contains the otp. 
					body = "OTP for verification of your email is {} .Thanks for visiting our Website.".format(otp)

					# try to send an email to the user provided email id
					try :	
						send_mail(
						    'Email Verification',
						    body,
						    'Website Manager',
						    [email],
						    fail_silently=False,
						)

					# if the error occur in sending email 	
					except socket.gaierror :

						#delete the newly created user from the database.
						user.delete()

						#and return the user to the register page with the below message.
						return render(request, "users/register.html", {
							"message": "Their is an error in sending Email at a time for verification. Please try after some time. ",
							"form": form,
							"button": "Register",
							"login": "Back"
						})

					# when the email successfully sent , return the register page with the otp form and with the below message.	
					return render(request, "users/register.html", {
						"message": "We have successfully delivered an OTP for Email Verification.",
						"form": OtpCheck(),
						"button": "Verify OTP"
						})	

				# If the user is registered with the user provided email and their activity status is False	
				if user.is_active == False :

					#delete the user from the database
					user.delete()

					#return register page with the below message.
					return render(request, "users/register.html", {
						"message": "Old Account Deleted. Create Password",
						"form": form,
						"button": "Register",
						"login": "Back"
						})

				# If the user is registered with the user provided email return the register page with the below message.	
				return render(request, "users/register.html", {
					"message": "Email Already Exist",
					"form": form,
					"button": "Register",
					"login": "Back"
					})

			# If the user is registered with the user provided username and their activity status is False	
			if user.is_active == False :

				#delete the user
				user.delete()

				#return register page with the below message.
				return render(request, "users/register.html", {
					"message": "Old Account Deleted. Create Password",
					"form": form,
					"button": "Register",
					"login": "Back"
					})

			# If the user is registered with the user provided username return the register page with the below message.	
			return render(request, "users/register.html", {
				"message": "Username Already Exist",
				"form": form,
				"button": "Register",
				"login": "Back"
			})	

		# Get all the data from otp check form.	
		otp = OtpCheck(request.POST)

		# if otp is valid to process
		if otp.is_valid():

			#get the user provided otp
			userotp = otp.cleaned_data['otp']

			#convert the otp to string
			userotp = str(userotp)

			#if otp does not contain only 6 characters
			if len(userotp) < 6 or len(userotp) > 6:

				#return the register page with the below message
				return render(request, "users/register.html", {
					"message": "OTP should contain only 6 numbers",
					"form": otp,
					"button": "Verify OTP"
					})

			#if otp contain 6 digits , try to get user with the user provided otp 	
			try :
				user = CustomUser.objects.get(otp=userotp)

			# if their is no user with the user provided otp	
			except CustomUser.DoesNotExist :

				#return the register page with the user provided otp and with the below message.
				return render(request, "users/register.html", {
					"message": "OTP did not match. Please try again.",
					"form": otp,
					"button": "Verify OTP"
					})

			# if their is the user in the database with the same otp
			# set its otp field with the below number	
			user.otp = 86197

			#save the user with the new otp			
			user.save()

			#return the user to the register page with the below message and with the details form.
			return render(request, "users/register.html", {
				"message": "OTP Validated. Please fill the details",
				"form": NamePhone(),
				"button": "Submit"
			})	

		# when user submitted the data in details form , get all the user submitted data	
		details = NamePhone(request.POST)

		#if the form is valid to process
		if details.is_valid():

			#get all the user provided data
			fname = details.cleaned_data['fname']					
			lname = details.cleaned_data['lname']
			number = details.cleaned_data['number']

			#convert number to string
			number = str(number)

			#if number does not contain 10 characters
			if len(number) < 10 or len(number) > 10 :

				#return register page with the user provided data and with the below message.
				return render(request, "users/register.html", {
					"message": "Mobile number must be of 10 digits only",
					"form": details,
					"button": "Submit"
				})	

			# get the user from the database with the otp = 86197	
			user = CustomUser.objects.get(otp=86197)

			#set that user fields with the user provided data
			user.first_name = fname
			user.last_name = lname
			user.number = number

			#set the otp to none or empty
			user.otp = None

			#set the user's activity status to True
			user.is_active = True

			#save the user with the new credentials
			user.save()

			#return the user login page with the below message
			return render(request, "users/login.html", {
				"form": LoginForm(),
				"message": "Your account is successfully registered."
				})

	#if user's request method = GET
	#return the user to register page with the register form.		
	return render(request, "users/register.html", {
		"form": RegisterForm(),
		"button": "Register",
		"login": "Back",
		})	

#Creating forgot view
def forgot(request):

	#if user is logged in , redirect the user to index page.
	if request.user.is_authenticated :
		return HttpResponseRedirect(reverse("users:index"))

	# if the user submits the form	
	if request.method == "POST":

		#get all the user submitted data
		User = UsernameOrEmail(request.POST)

		#if data is valid to process 
		if User.is_valid():

			#get the user provided data ,ie, the username or email
			username = User.cleaned_data["username"]

			#set set username key to the user provided username
			kwargs = {'username':username}

			#if the user provided data contains an "@" in it
			if '@' in username:

				#set the email key with the user provided username
				kwargs = {'email':username}

			#try to get the user with the user provided data	
			try :	
				user = CustomUser.objects.get(**kwargs)

			# if their is no user in the database with the user provided data
			except CustomUser.DoesNotExist:

				#return the user to forgot page with the below message.
				return render(request, "users/forgotpass.html", {
				"message": "User Does Not Exist",
				"form": User,
				"button": "Verify Acoount"
				})

			#if their is an user in the database
			#get the email of the database user	
			email = user.email

			#generate 6 digits random otp
			otp = random.randint(100000 , 999999)

			#save the otp to the user otp field in database
			user.otp = otp

			#save the user with the new otp
			user.save()

			#create the body of an email with the otp
			body = "OTP to change your password is {} .Thanks for visiting our Website.".format(otp)

			#try to send email to the user's email
			try :
				send_mail(
				    'Email Verification',
				    body,
				    'Website Manager',
				    [email],
				    fail_silently=False,
				)

			#if their is an error in sending email	
			except socket.gaierror :

				#return the user to the forgot page with the below message
				return render(request, "users/forgotpass.html", {
				"message": "Their is an error in sending Email at a time for verification. Please try after some time. ",
				"form": User,
				"button": "Verify Acoount"
				})

			#when email successfully sent , open forgot page with the otp check form and with the below messsage.	
			return render(request, "users/forgotpass.html", {
				"message": "We have successfully delivered an OTP to your registered Email ID ",
				"form": OtpCheck(),
				"button": "Verify OTP"
				})

		# when user submits otp , get all the data from the form	
		otp = OtpCheck(request.POST)

		#if form is valid to process
		if otp.is_valid():

			#get the user provided otp from the form
			userotp = otp.cleaned_data['otp']

			#convert otp to string
			userotp = str(userotp)

			#if otp doesnot contain only 6 characters
			if len(userotp) < 6 or len(userotp) > 6:

				#return the user to forgot page with the user provided otp and with the below message
				return render(request, "users/forgotpass.html", {
					"message": "OTP should contain only 6 numbers",
					"form": otp,
					"button": "Verify OTP"
					})

			#try to get the user with the user provided otp	
			try :
				user = CustomUser.objects.get(otp=userotp)

			# if their is no user	
			except CustomUser.DoesNotExist :

				#return the forgot page with the below message
				return render(request, "users/forgotpass.html", {
					"message": "OTP did not match. Please try again.",
					"form": otp,
					"button": "Verify OTP"
					})	

			#if we get the user	
			#set the user otp to 86197
			user.otp = 86197

			#save the user with the new otp	
			user.save()

			#return user the forgot page with the password form and with the below message
			return render(request, "users/forgotpass.html", {
			"message": "OTP Validated. Now you can change your password",
			"form": Password(),
			"button": "Change Password"
			})

		#when password form submits get all the data	
		password = Password(request.POST)

		#if form is valid to process
		if password.is_valid():

			#get the user provided data
			newpass = password.cleaned_data['password']	
			confirm = password.cleaned_data['confirm']

			#if password and confirm is not equal
			if newpass != confirm:

				#return the forgot page again with the password form and with the below message
				return render(request, "users/forgotpass.html", {
				"message": "Password did not match. Try again.",
				"form": Password(),
				"button": "Change Password"
				})

			#if password matched
			#get the user with the below otp	
			user = CustomUser.objects.get(otp=86197)

			#set password of the user to the user provided password
			user.set_password(newpass)

			#set otp of the user to none or empty
			user.otp = None

			#save the user with the new credentials
			user.save()

			#return the user to login page with the below messsage
			return render(request, "users/login.html", {
				"message": "Password Changed Successfully",
				"form": LoginForm()
				})

	# if user request method is GET		
	#return the user forgot page.
	return render(request, "users/forgotpass.html", {
		"form": UsernameOrEmail(),
		"button": "Verify Acoount"
		})	