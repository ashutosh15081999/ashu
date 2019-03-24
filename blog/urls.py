from django.urls import include, path
from .views import *
urlpatterns = [
	
    path('home/', PostListView.as_view(), name="blog_home"),
    path('about/', about, name = "blog_about"),
    path('post/<int:pk>/',PostDetailView.as_view(), name="post-content"),
    path('post/new/',PostCreateView.as_view(), name="post-ccreate"),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name="post-delete"),
]