from django.urls import path
from . import views

urlpatterns=[
  path("", views.home, name="home"),
  path("posts/", views.posts, name="posts"),
  path("posts/postDetails/<int:id>", views.postDetails, name="postDetails"),
  path("posts/postDetails/editPost/<int:id>", views.editPost, name="editPost"),
  path("posts/newPost/", views.newPost, name="newPost"),

]