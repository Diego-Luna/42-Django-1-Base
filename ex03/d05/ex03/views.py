from django.shortcuts import render
from .utils import generate_shader

# Create your views here.
def index(request):
    
    colors_shades = generate_shader()
    color_names = ['noir', 'rouge', 'bleu', 'vert']

    context ={
        'colors_shades': colors_shades,
        'color_names': color_names,
    }

    return render(request, 'index.html', context)