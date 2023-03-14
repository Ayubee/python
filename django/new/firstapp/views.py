from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse("hello world")

def about (request):
    return HttpResponse("<h2>about<h2/>")

def contact (request):
    return HttpResponse("contact")
