from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html') #Esto es necesario para seguir con la arquitectura cliente-servidor.
