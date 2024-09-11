from django.shortcuts import render
from rest_framework import viewsets
from home.serializers import TopicoSerializer
from home.models import Topico
#from django.http import HttpResponse
# Create your views here.

class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer

def home(request):
    #testeHome = '<p>teste home</p>'
    contexto = {
        'title' : '✂️ Shorties',
        'artigos': Topico.objects.all()
    }
    return render(request, 'home/index.html', contexto)


# def artigo(request):
#     exibe_artigos = {
#         'artigos': Topico.objects.all()
#     }

#     return render(
#         request,
#         'home/index.html',
#         exibe_artigos,
#     )


