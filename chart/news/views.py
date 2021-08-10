from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django_currentuser.middleware import get_current_authenticated_user
from .models import Post
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


def get_user_settings_posts_per_page(user):
    """ Unauthenticated user has no attribute user_setting_pages """
    try:
        user_setting_pages = user.profile.posts_per_page
    except AttributeError:
        user_setting_pages = 5

    return user_setting_pages


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'news/home.html'
    context_object_name = 'news'
    queryset = Post.objects.filter(is_public=True).order_by('-date_posted')

    def get_paginate_by(self, *args, **kwargs):
        user = get_current_authenticated_user()
        return get_user_settings_posts_per_page(user)


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'news/user_posts.html'
    context_object_name = 'news'

    def get_paginate_by(self, *args, **kwargs):
        user = get_current_authenticated_user()
        return get_user_settings_posts_per_page(user)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('/news')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('/news')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def blog(request):
    return render(request, 'news/blog.html')
