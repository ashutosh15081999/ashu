from django.urls import include, path
from .views import *
urlpatterns = [
	path('books/', PostListView.as_view(), name="book_home"),
    path('home/', home, name="user_reg"),
    path('book/<int:pk>/',PostDetailView.as_view(), name="book-content"),
    path('book/new/',PostCreateView.as_view(), name="book-ccreate"),
    path('book/<int:pk>/delete/',PostDeleteView.as_view(), name="book-delete"),
    path('book/email/',email,name="send-email"),
    #path('book/don/',useless,name="useless"),
    #path('book/<int:pk>/delete/', delete, name = "delete"),
]