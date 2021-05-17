from django import forms
from django.forms import ModelForm
from users.models import CustomUser
#Login Page Form :-
class LoginForm(forms.Form):
	username = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Username or Email ID","autofocus": True}))
	password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"placeholder":"Password"}))

#OTP Verification Form :-
class OtpCheck(forms.Form):	
	otp = forms.IntegerField(label="",widget=forms.NumberInput(attrs={"placeholder":"Enter Your OTP","autofocus": True}))

#Forgot Password Forms Started :-
class UsernameOrEmail(forms.Form):
	username = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Username or Email ID","autofocus": True}))


class Password(forms.Form):	
	password = forms.CharField(min_length=8,label="",widget=forms.PasswordInput(attrs={"placeholder":"Password","autofocus": True}))
	confirm = forms.CharField(min_length=8,label="",widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
#Forgot Password Forms Ended /-

#Register Page Form Started :-
class RegisterForm(forms.Form):
	username = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Username","autofocus": True}))
	email = forms.CharField(label="",widget=forms.EmailInput(attrs={"placeholder":"Email"}))
	password = forms.CharField(min_length=8,label="",widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
	confirm = forms.CharField(min_length=8,label="",widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

class NamePhone(forms.Form):
	fname = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"First Name","autofocus": True}))
	lname = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Last Name"}))
	number = forms.IntegerField(label="",widget=forms.NumberInput(attrs={"placeholder":"Phone Number"}))
#Register Page Form Ended:-	
