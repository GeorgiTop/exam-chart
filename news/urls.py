from django.urls import path
from . import views

import news.views

urlpatterns = [
    path('', views.home, name='news-home'),
    path('video/', views.video, name='news-video'),
    path('blog/', views.blog, name='news-blog'),
]
