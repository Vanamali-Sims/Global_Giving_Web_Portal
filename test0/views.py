from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def viewme(request):
    return HttpResponse("Im your dad")