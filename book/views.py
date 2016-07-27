from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm 

def login_page(request):
	return render(request,'login_page.html')

def log_check(request):

	username = request.POST.get('username')  
	password = request.POST.get('password')
	user = authenticate(username = username, password = password )
	if user is not None:
			login(request, user)
			return HttpResponseRedirect('login_sucess')
	else:
				return HttpResponseRedirect ('invalid')