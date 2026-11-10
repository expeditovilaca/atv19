from django.urls import path
from . import views

urlpatterns = [
    path('categorias/cadastrar/', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('categorias/<int:pk>/editar/', views.atualizar_categoria, name='atualizar_categoria'),
    path('categorias/<int:pk>/excluir/', views.excluir_categoria, name='excluir_categoria'),
    
    path('tags/cadastrar/', views.cadastrar_tag, name='cadastrar_tag'),
    path('tags/<int:pk>/editar/', views.atualizar_tag, name='atualizar_tag'),
    path('tags/<int:pk>/excluir/', views.excluir_tag, name='excluir_tag'),
]