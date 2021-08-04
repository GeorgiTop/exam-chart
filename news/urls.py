from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('new/', views.PostCreateView.as_view(), name='blog-create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='blog-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='blog-delete'),
    path('video/', views.video, name='blog-video'),
    path('blog/', views.blog, name='blog-blog'),
]
