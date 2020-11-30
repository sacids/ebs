from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .utils import *

# Create your views here.


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # redirect
            if(is_respondent(user)):
                return redirect('/questionnare')
            elif(is_reviewer(user)):
                return redirect('/responses/countries/')
        else:
            messages.error(request, 'Username OR Password is incorectly')

    context = {}
    return render(request, 'accounts/login.html', context)
