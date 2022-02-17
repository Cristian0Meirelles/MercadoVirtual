from django.contrib import admin
<<<<<<< HEAD
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
=======

# Register your models here.
>>>>>>> 6e228b040c0547109feeef39169e8d63f77aa828
