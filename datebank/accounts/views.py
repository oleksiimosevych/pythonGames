from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
#to add additional fields to user
from django.contrib.auth.models import User
#to reg Betreiber
from certification82.models import Betreiber
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
# from datebank.forms import SignUpForm

# Create your views here.
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			# email = form.cleaned_data.get('EZA_Betreiber_Mail')
			# first_last_name = form.cleaned_data.get('first_name')

			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})


# class SignUp(generic.CreateView):
# 	form_class = UserCreationForm
# 	success_url = reverse_lazy('login')
# 	template_name = 'registration/signup.html'

# #to add additional fields to user
# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )