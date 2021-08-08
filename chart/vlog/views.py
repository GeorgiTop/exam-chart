from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django_currentuser.middleware import get_current_authenticated_user

from .models import VlogPost


def get_user_settings_posts_per_page(user):
    """ Unauthenticated user has no attribute user_setting_pages """
    try:
        user_setting_pages = user.profile.posts_per_page
    except AttributeError:
        user_setting_pages = 5

    return user_setting_pages


class VlogPostListView(ListView):
    model = VlogPost
    template_name = 'vlog/vlogpost_home.html'
    context_object_name = 'vlogs'
    # queryset = VlogPost.objects.filter(is_public=True).order_by('-date_posted')
    slug_field = 'slug'

    def get_paginate_by(self, *args, **kwargs):
        user = get_current_authenticated_user()
        return get_user_settings_posts_per_page(user)

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return VlogPost.objects.order_by('-date_posted')
        else:
            return VlogPost.objects.filter(is_public=True).order_by('-date_posted')


class UserVlogPostListView(LoginRequiredMixin, ListView):
    model = VlogPost
    template_name = 'vlog/user_vlogposts.html'
    context_object_name = 'vlogs'

    def get_paginate_by(self, *args, **kwargs):
        user = get_current_authenticated_user()
        return get_user_settings_posts_per_page(user)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return VlogPost.objects.filter(author=user).order_by('-date_posted')


class VlogPostCreateView(LoginRequiredMixin, CreateView):
    model = VlogPost
    fields = [
        'song_name',
        'artist_name',
        'music',
        'lyrics',
        'arranged',
        'producer',
        'video_url',
        'spotify',
        'itunes',
        'is_public'
    ]
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class VlogPostDetailView(LoginRequiredMixin, DetailView):
    model = VlogPost
    slug_field = 'slug'


class VlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = VlogPost
    slug_field = 'slug'
    fields = [
        'song_name',
        'artist_name',
        'music',
        'lyrics',
        'arranged',
        'producer',
        'video_url',
        'spotify',
        'itunes',
        'is_public'
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class VlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = VlogPost
    success_url = '/video/'
    slug_field = 'slug'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
