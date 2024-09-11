from django.shortcuts import render
from .models import Pessoa

def comentarios(request):
    contexto = {
        'title' : '✂️ Shorties',
    }
    return render(request, 'comentarios/comentarios.html', contexto)

def gravar(request):
    nome_error = comentario_error = ''
    nome = request.POST.get('nome')
    comentario = request.POST.get('comentario')

    if not nome:
        nome_error = 'erro'
    if not comentario:
        comentario_error = 'erro'

    if nome_error or comentario_error:
        contexto = {
            'nome_error' : nome_error,
            "comentario_error" : comentario_error,
            'msg_error' : 'Entre com valores válidos',
            'nome' : nome,
            'comentario' : comentario,
        }
        return render (request, 'comentarios/comentarios.html', contexto)

    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.comentario = request.POST.get('comentario')
    nova_pessoa.save()

    return exibe(request)

def exibe(request):
    
    exibe_pessoas = {
        'pessoas': Pessoa.objects.all()
    }
    return render(request, 'comentarios/comentarios.html', exibe_pessoas) 


def atualizar(request, id):
    nova_pessoa = Pessoa.objects.get(id_pessoa=id)
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.comentario = request.POST.get('comentario')
    nova_pessoa.save()

    return exibe(request)

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    
    return render(request, 'comentarios/editar.html', {"pessoa": pessoa}) 

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()

    return exibe(request) 

# def localizar(request):
#     if request.method =='POST':
#         try:
#             id = request.POST.get('id')  
#             pessoa = Pessoa.objects.get(id_pessoa=id)
#             contexto = {"pessoa": pessoa}
#         except Exception:  
#             contexto = {"erro": "Registro não encontrado"}
#     else:
#         contexto =  {}
   
#     return render(
#         request,
#         'contato/localizar.html',
#         contexto,
#     )

# def localizarmais(request):
#     if request.method == 'POST':
#         selecao = request.POST.get('tbusca')
#         busca = request.POST.get('busca')
#         pessoas = []  # Lista vazia para armazenar os resultados da pesquisa
#         try:
#             if selecao == 'id':  
#                 pessoa = Pessoa.objects.get(id_pessoa=busca)
#                 pessoas.append(pessoa)
#             elif selecao == 'nome':
#                 pessoas = Pessoa.objects.filter(nome=busca)           
           
#             contexto = {"pessoas": pessoas, "busca": busca}
#         except Exception:
#             contexto = {"erro": "Registro não encontrado", "busca": busca}
#     else:
#         contexto = {}  # Inicializa contexto vazio na primeira vez do carregamento


#     return render(
#         request,
#         'contato/localizarmais.html',
#         contexto,
#     )
