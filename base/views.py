from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def takList(resquest):
    return HttpResponse('Task List view')