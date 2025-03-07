from django.shortcuts import render

def django_view(request):
    return render(request, 'pages/django.html')

def display_view(request):
    return render(request, 'pages/display.html')

def templates_view(request):
    return render(request, 'pages/templates.html')
