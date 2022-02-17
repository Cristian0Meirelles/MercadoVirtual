from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class ItensSelecionadosForm(forms.ModelForm):
    class Meta:
        model = ItensSelecionados
        fields = "__all__"

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = "__all__"


