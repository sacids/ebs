from django.http import request
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(None,'index.html', {})
