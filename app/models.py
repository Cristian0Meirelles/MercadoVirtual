from django.db import models
from django.forms import IntegerField

# Create your models here.

CATEGORIA_CHOICES = (
    ('1','Frutas'),
    ('2','Bebidas'),
    ('3','Alimento Não Perecível'),
    ('4', 'Alimento Perecível')

)


class   User(models.Model):
    nome = models.CharField(max_length=96, blank = True, null = True)
    cpf = models.CharField(max_length=24, blank = True, null = True)
    email = models.EmailField(blank = True, null = True)
    def __str__(self):
        return self.nome

class Item(models.Model):
    nome_item = models.CharField(max_length=100, blank = True, null = True)
    categoria = models.CharField(choices=CATEGORIA_CHOICES, max_length=50, blank = True, null = True)
    valor = models.CharField(IntegerField,max_length=24, blank = True, null = True)
    def __str__(self):
        return self.nome_item

class Pagamento(models.Model):
    PAGAMENTO_CHOICES =(
        ('1','Credito'),
        ('2','Debito'),
        ('3','Pix')
    )
    idCliente = models.ForeignKey(User, on_delete=models.SET_NULL, blank = True, null = True)
    data = models.DateTimeField(auto_now_add=True, blank = True, null = True)
    preço =  models.CharField(IntegerField, max_length=24, blank=True, null = True)
    tipo_pagamento = models.CharField(choices=PAGAMENTO_CHOICES, max_length=50, blank=True, null = True)
    
    def __str__(self):
        return str("Pagamento " + str({self.pk}))

class ItensSelecionados(models.Model):
    pedidos = models.ForeignKey(Pagamento, on_delete=models.CASCADE, blank = True, null = True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank = True, null = True)
    quantidade = models.PositiveIntegerField(default=1)

    
    
  
    
    
    