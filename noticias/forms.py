from django import forms
from .models import Categoria, Tag

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['nome']