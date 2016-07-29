from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 
from .forms import Register_user

def login_page(request):
	return render(request,'login_page.html')

def log_check(request):

	username = request.POST.get('username')  
	password = request.POST.get('password')
	user = authenticate(username = username, password = password )
	if user is not None:
			login(request, user)
			return HttpResponseRedirect('login success')
	else:
				return HttpResponseRedirect ('invalid username or password')

def log_out(request):
	return render (request,'login_page.html')

def invalid_user(request):
	return render (request,'invalid_user_page.html')

def user_signup(request):
	if request.method == 'POST':
		form = Register_user(request.POST)
		if form.is_valid:
			form.save()
			return HttpResponseRedirect('signupsuccessfully')
		else:
			return HttpResponse('invalid data')

	args={}
	args['form']= Register_user()
	return render (request,'user_signup.html',args)