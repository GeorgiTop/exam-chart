from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='news-home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('new/', views.PostCreateView.as_view(), name='news-create'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='news-delete'),
    path('news/', views.blog, name='news-news'),
]
