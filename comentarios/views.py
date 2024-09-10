from django.shortcuts import render
from .models import Pessoa

def comentarios(request):
    contexto = {
        'title' : '✂️ Shorties',
    }
    return render(request, 'comentarios/comentarios.html', contexto)

def gravar(request):
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.comentario = request.POST.get('comentario')
    nova_pessoa.save()

    return comentarios(request)

def exibe(request):
    exibe_pessoas = {
        'pessoas': Pessoa.objects.all()
    }
    return render(request, 'comentarios/mostrar.html', exibe_pessoas) 