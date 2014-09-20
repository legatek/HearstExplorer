from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def browse(request):
    return HttpResponse("Hello, world. You're at the Image By Browse index.")