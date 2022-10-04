from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post



# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'index.html'


class HomePageViewDetail(DetailView):
    model = Post
    template_name = 'about.html'

class CreatePageView(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'author', 'body', 'date']


class UpdatePageView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body']


class DeletePageView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')