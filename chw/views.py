from django.shortcuts import render

from cal.forms import *
from cal.models import *

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, get_user

def auth_login(request):
    context = {}
    context['next'] = request.GET.get('next', False)
    if request.method == 'POST':
        form = LoginForm(request.POST)
    else:
        form = LoginForm()
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            if request.POST.get('next', False):
                return HttpResponseRedirect(request.POST.get('next', False))
            else:
                return HttpResponseRedirect(reverse('index'))
    context['form'] = form
    return render(request, 'login.html', context)

def auth_signup(request):
    return render(request, 'signup.html', {})