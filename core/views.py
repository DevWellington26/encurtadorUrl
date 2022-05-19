from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect

from .models import Link

def home(request):
    if request.method == 'POST':
        acao = request.POST.get('acao')
        if acao == 'cadastrar':
            nome = request.POST.get('nome')
            link = request.POST.get('link')
            novo_link = Link()
            novo_link.nome = nome
            novo_link.link = link
            novo_link.save()
            return render(request, 'index.html', {'acao':'cadastrar', 'nome':nome, 'link': link})
    elif request.method == 'GET':
        return render(request, 'index.html')

def redirect(request, nome):
    link_selecionado = Link.objects.get(nome__exact=nome)
    print(link_selecionado)
    if link_selecionado:
        return HttpResponseRedirect(link_selecionado.link)
    else:
        return HttpResponseRedirect('/')
