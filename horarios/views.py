from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def horarios(request):
    contexto = {
        'title' : 'Shorties',
        'text' : 'HORARIOS'
    }
    return render(request, 'horarios/index.html', contexto)