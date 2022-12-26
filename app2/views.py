from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def function3(request):
    return HttpResponse('this my first view in app2')
def function4(request):
    return HttpResponse('this my second view in app2')
