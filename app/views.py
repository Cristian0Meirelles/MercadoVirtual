from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView
from django.forms import inlineformset_factory

def index(request):
    num_user = User.objects.all().count()
    num_itens = Item.objects.all().count()
    num_pagamentos =  Pagamento.objects.all().count()
    
    context = {
        'num_user': num_user,
        'num_itens': num_itens,
        'num_pagamento': num_pagamentos,

        
    }
    template_name = 'home.html'
    return render(request, template_name, context) 

class listaUser(ListView):
    template_name = 'lista_user.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.all()    

class detalhesUsers(DetailView):
    model = User
    template_name ='user_Detalhes.html'

def cadastroUsers(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('User')
    form = UserForm()

    return render(request,'cadastro.html',{'form': form})

def editarUsers(request, pk, template_name='cadastro.html'):
    users = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=users)
    if form.is_valid():
        form.save()
        return redirect('User')
    return render(request, template_name, {'form':form})    

def excluirUsers(request, pk, template_name='confirm_delete.html'):
    user = get_object_or_404(User, pk=pk)
    if request.method=='POST':
        user.delete()
        return redirect('User')
    return render(request, template_name, {'object':user})




class listaPagamento(ListView):
    template_name = 'lista_Pagamento.html'
    context_object_name = 'lista_Pagamento'

    def get_queryset(self):
        return Pagamento.objects.all()   

def checkUser(nome):
    users = User.objects.all()

    for x in users:
        if x.nome == nome:
            return x.pk

    return "DONT_EXIST"

def buscaUser(request):
    if request.method == 'POST':
        nome = request.POST["nome"]
        userId = checkUser(nome)
        if userId != "DONT_EXIST":
            url = "add/" + str(userId)
            return redirect(url)
        else:
            return render(request, 'user_Erro.html')
    return render(request, 'user_Busca.html')

def cadastroPagamento(request, pk):
    movimento_forms = Pagamento()
    item_movimento_formset = inlineformset_factory(Pagamento, ItensSelecionados, form=ItensSelecionadosForm, extra=0, can_delete=False, min_num=1, validate_min=True)

    if request.method == 'POST':
        forms = PagamentoForm(request.POST, request.FILES, instance=movimento_forms, prefix='main')
        formset = item_movimento_formset(request.POST, request.FILES, instance=movimento_forms, prefix='item')

        if forms.is_valid() and formset.is_valid():
            forms = forms.save(commit=False)
            forms.idUser = User.objects.get(pk=pk)
            forms.save()
            formset.save()
            url = "../../pagamento/" + str(forms.pk)
            return redirect(url)

    else:
        forms = PagamentoForm(instance=movimento_forms, prefix='main')
        formset = item_movimento_formset(instance=movimento_forms, prefix='item')

    context = {
        'forms': forms,
        'formset': formset,
    }

    return render(request, 'cadastro_Pagamento.html', context)

def detalhesPagamento(request, pk):
    template_name = 'detalhes_Pagamento.html'
    pagamento = Pagamento.objects.get(pk=pk)
    itensSelec = ItensSelecionados.objects.get_queryset().filter(pagamento=pk)
    context = {
        'pagamento': pagamento,
        'ItenSelec': itensSelec,
    }
    return render(request, template_name, context)                             

def excluirPagamento(request, pk, template_name='confirm_delete.html'):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    if request.method=='POST':
        pagamento.delete()
        return redirect('Pagamento')
    return render(request, template_name, {'object':pagamento})




class listaItem(ListView):
    template_name = 'list_itens.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()  

def cadastroItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Item')
    form = ItemForm()

    return render(request,'cadastro.html',{'form': form})

def editarItem(request, pk, template_name='cadastro.html'):
    itens = get_object_or_404(Item, pk=pk)
    form = ItemForm(request.POST or None, instance=itens)
    if form.is_valid():
        form.save()
        return redirect('Item')
    return render(request, template_name, {'form':form})     

def excluirItem(request, pk, template_name='confirm_delete.html'):
    item = get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('Item')
    return render(request, template_name, {'object':item})    