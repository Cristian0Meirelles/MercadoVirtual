from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email')
    fields = ['nome', 'cpf', 'email']

admin.site.register(User, UserAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome_item', 'categoria','valor')
    fields = ['nome_item', 'categoria','valor']

admin.site.register(Item, ItemAdmin)