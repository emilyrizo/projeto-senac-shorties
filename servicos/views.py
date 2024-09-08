from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def servicos(request):
    contexto = {
        'title' : '✂️ Shorties',
    }
    return render(request, 'servicos/index.html', contexto)
