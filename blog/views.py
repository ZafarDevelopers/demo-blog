import pyperclip
from django.shortcuts import render, redirect
from . models import Post
from . forms import postForm

def home(request):
  return render(request, "home.html")

def posts(request):
  post= Post.objects.all()
  return render(request, "posts.html", {"post": post})

def postDetails(request, id):
  post = Post.objects.get(id=id)
  text=str(post)
  copy= pyperclip.copy(text)
  return render(request, "postDetails.html", {"post": post}, {"copy": copy})

def newPost(request):
  context={}
  context["form"] =postForm()
  if request.method=="POST":
    form = postForm(request.POST)
    if form.is_valid():
      post= form.save(commit=False)
      post.author =request.user 
      post.save()
      return redirect(postDetails)
    else:
      form = postForm()

  return render(request, "newPost.html", context)

def editPost(request, id):
  post= Post.objects.get(id=id)
  context={}
  context["edit"]=postForm()
  if request.method=="POST":
    form=postForm(request.POST, instance=posts)
    if form.is_valid():
      edit=post.save(commit=False)
      edit.author=request.user
      edit.save()
      return redirect(postDetails)
    else:
      form=postForm(instance=posts)
  return render(request, "editPost.html", context, {"post": post})


# Create your views here.
