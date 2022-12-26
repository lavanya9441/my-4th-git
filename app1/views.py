from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def function1(request):
    return HttpResponse('this my first view in app1')
def function2(request):
    return HttpResponse('this my second view in app1')
