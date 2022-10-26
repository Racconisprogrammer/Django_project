# Create your models here.from distutils.log import Log
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def index(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})

class HomePageView(ListView):
    model = Post
    template_name = 'index.html'


class HomePageViewDetail(DetailView):
    model = Post
    template_name = 'about.html'

class CreatePageView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'body', 'author']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool:
        return self.request.user.is_superuser


class UpdatePageView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'body', 'photo']

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.author == self.request.user


class DeletePageView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.author == self.request.user
        