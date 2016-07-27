from django.shortcuts import render

def login_page(request):
	return render(request,'templates/login_page.html')

def log_check(request):
	
	username = request.POST.get('username')  
		password = request.POST.get('password')
		user = authenticate(username = username, password = password )
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('loggedin')
		else:
				return HttpResponseRedirect ('invalid')