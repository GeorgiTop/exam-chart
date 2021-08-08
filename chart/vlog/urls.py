from django.urls import path
from . import views

urlpatterns = [
    path('', views.VlogPostListView.as_view(), name='vlog-home'),
    path('user/<str:username>', views.UserVlogPostListView.as_view(), name='user-vlog-posts'),
    path('new/', views.VlogPostCreateView.as_view(), name='vlog-create'),
    path('<slug:slug>/', views.VlogPostDetailView.as_view(), name='vlog-detail'),
    path('<slug:slug>/update', views.VlogPostUpdateView.as_view(), name='vlog-update'),
    path('<slug:slug>/delete', views.VlogPostDeleteView.as_view(), name='vlog-delete'),
]
