from django.shortcuts import render
from django.conf import settings
from datetime import datetime
import os
from .forms import TextForm

def index(request):
    
    # ! 1. Crear el archivo de logs si no existe
    if not os.path.exists(settings.EX02_LOG_PATH):
        os.makedirs(os.path.dirname(settings.EX02_LOG_PATH), exist_ok=True)
        with open(settings.EX02_LOG_PATH, 'w') as file:
            pass

    # * 2. create the form object with the place holder and the history
    form = TextForm()
    history = []
    
    # * 3. Cargar historial existente
    try:
        with open(settings.EX02_LOG_PATH, 'r') as file:
            history = [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"Error al leer el archivo de logs: {e}")
    
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{timestamp}] {form.cleaned_data['text']}"
            
            # * Guardar en archivo de logs
            with open(settings.EX02_LOG_PATH, 'a') as file:
                file.write(log_entry + '\n')
            
            # * Actualizar historial
            history.append(log_entry)
    
    context = {
        'form': form,
        'history': history
    }
    
    return render(request, 'ex02/index.html', context)