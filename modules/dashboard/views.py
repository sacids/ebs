from django.contrib import auth
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    print(request.user.username)
    print(request.user.first_name)
    print(request.user.last_name)
    return render(request,'index.html', {})
