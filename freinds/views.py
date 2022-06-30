from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showdata(request):
  return HttpResponse('Hi my friends')


def showdatafs(re):
  return HttpResponse('I have not my freinds ')

def testfun(r):
  return HttpResponse('I want you')