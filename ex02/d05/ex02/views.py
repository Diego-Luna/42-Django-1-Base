from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def django_view(request):
    # Todo: show a hello work
    return HttpResponse('Hello World')