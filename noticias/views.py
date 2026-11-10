# noticias/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import ProtectedError
from .models import Categoria, Tag
from .forms import CategoriaForm, TagForm

# --- GERENCIAMENTO DE CATEGORIAS ---

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria cadastrada com sucesso!")
            return redirect('cadastrar_categoria')
        else:
            messages.error(request, "Por favor, corrija os erros do formulário abaixo.")
    else:
        form = CategoriaForm()
    return render(request, 'categorias/form.html', {'form': form})

def atualizar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "Categoria atualizada com sucesso!")
            return redirect('cadastrar_categoria')
        else:
            messages.error(request, "Por favor, corrija os erros do formulário abaixo.")
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/form.html', {'form': form})

def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, "Categoria excluída com sucesso!")
            return redirect('cadastrar_categoria')
        except ProtectedError:
            messages.error(request, "Não é possível excluir esta categoria, pois existem notícias vinculadas a ela.")
            return redirect('cadastrar_categoria')
            
    return render(request, 'categorias/confirmar_exclusao.html', {'categoria': categoria})


# --- GERENCIAMENTO DE TAGS ---

def cadastrar_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag cadastrada com sucesso!")
            return redirect('cadastrar_tag')
        else:
            messages.error(request, "Por favor, corrija os erros do formulário abaixo.")
    else:
        form = TagForm()
    return render(request, 'tags/form.html', {'form': form})

def atualizar_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            messages.success(request, "Tag atualizada com sucesso!")
            return redirect('cadastrar_tag')
        else:
            messages.error(request, "Por favor, corrija os erros do formulário abaixo.")
    else:
        form = TagForm(instance=tag)
    return render(request, 'tags/form.html', {'form': form})

def excluir_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    if request.method == 'POST':
        tag.delete()
        messages.success(request, "Tag excluída com sucesso!")
        return redirect('cadastrar_tag')
        
    return render(request, 'tags/confirmar_exclusao.html', {'tag': tag})