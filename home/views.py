from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def home(request):
    #testeHome = '<p>teste home</p>'
    contexto = {
        'title' : '✂️ Shorties'
    }
    return render(request, 'home/index.html', contexto)


