from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    tempalte = loader.get_template('index.html')
    return HttpResponse(tempalte.render(None, request))