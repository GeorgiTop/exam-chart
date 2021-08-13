from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsPostListView.as_view(), name='news-home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name='user-posts'),
    path('new/', views.NewsPostCreateView.as_view(), name='news-create'),
    path('<int:pk>/', views.NewsPostDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsPostUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsPostDeleteView.as_view(), name='news-delete'),
    # path('news/', views.blog, name='news-news'),
]
