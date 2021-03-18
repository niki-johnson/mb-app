from django.shortcuts import render
#importando um class-based generico que sera usado para listar os conteudos da basede dados
from django.views.generic import ListView

from.models import Post

# Create your views here.
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    #explicitando o nome da lista
    context_object_name = 'all_posts_list'
    