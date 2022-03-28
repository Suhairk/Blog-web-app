from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),                         #SEE THE all POST ok
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'), #user post
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),       #see individual post details ok
    path('post/new/', PostCreateView.as_view() , name = 'post-create' ),                #create new post ok
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),        #update post ok
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),        #delete post ok
    path('media/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),          #search
    path('search/', views.search, name='search'),                                   #about
]
