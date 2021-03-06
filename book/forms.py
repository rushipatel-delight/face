from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register_user(UserCreationForm):
	email = forms.EmailField(required= True)
	class Meta: 
		model = User
		fields = ('username','email','password1','password2')
	def save(self, commit=True):
		user = super(Register_user,self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()
		return user