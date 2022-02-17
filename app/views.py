from django.shortcuts import render

from .models import *
from .forms import *

def index(request):
    num_user = User.objects.all().count()
    num_itens = Item.objects.all().count()
    num_pagamentos =  Pagamento.objects.all().count()
    num_itenselecionados = ItensSelecionados.objects.all().count()
    context = {
        'num_user': num_user,
        'num_itens': num_itens,
        'num_pagamento': num_pagamentos,
        'num_itenselecionados': num_itenselecionados
    }
    template_name = 'home.html'
    return render(request, template_name, context) 
