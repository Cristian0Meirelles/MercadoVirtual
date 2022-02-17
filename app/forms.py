from django import forms
from .models import *


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class ItensSelecionadosForm(forms.ModelForm):
    class Meta:
        model = ItensSelecionados
        fields = ["__all__"]

