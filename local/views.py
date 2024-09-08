from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def local(request):
    contexto = {
        'title' : 'BarberQueer',
    }
    return render(request, 'local/index.html', contexto)
