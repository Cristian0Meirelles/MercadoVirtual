from django.shortcuts import render
<<<<<<< HEAD
from .models import *
from .forms import *

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

=======

# Create your views here.
>>>>>>> 6e228b040c0547109feeef39169e8d63f77aa828
