from django.shortcuts import render, redirect
from .models import Post, Devtool

# Create your views here.
def idealist(request):
  posts = Post.objects.all()
  order = request.GET.get("order","None")
  if order == "title":
    posts = posts.order_by("title")
  elif order == "created":
    posts = posts.order_by("created_at")
  elif order == "updated":
    posts = posts.order_by("-created_at")
  else:
    posts = posts.order_by("title")

  context = {"posts":posts}
  return render(request, template_name="posts/idealist.html", context=context)

def idearegister(request):
  lists = Devtool.objects.all()
  if request.method == "POST":
    title = request.POST["title"]
    req_image = request.FILES["image"]
    content = request.POST["content"]
    interest = request.POST["interest"]
    devtool = request.POST["devtool"]
    for list in lists:
      print(list)
      if list.name == devtool:
        devtool = list

    Post.objects.create(title=title, image=req_image, content=content, interest=interest, devtool=devtool)
    return redirect("/")

  devtoollist = []
  for list in lists:
    devtoollist.append(list.name)
  context={"devtools":devtoollist}

  return render(request, template_name="posts/idearegister.html", context=context)

def ideadetail(request, id):
  post = Post.objects.get(id=id)
  devtool_name = post.devtool.name
  devtool = post.devtool
  all_post = devtool.post_devtool.all()
  context = {
    "post": post,
    "devtool_name": devtool_name,
    "all_post": all_post,
    }
  return render(request, template_name="posts/ideadetail.html", context=context)

def ideaupdate(request, id):
  lists = Devtool.objects.all()
  if request.method == "POST":
    title = request.POST["title"]
    req_image = request.FILES["image"]
    content = request.POST["content"]
    interest = request.POST["interest"]
    devtool = request.POST["devtool"]

    for list in lists:
      print(list)
      if list.name == devtool:
        devtool = list

    Post.objects.filter(id=id).update(title=title, image=req_image, content=content, interest=interest, devtool=devtool)
    return redirect(f"/ideadetail/{id}")

  elif request.method == "GET":
    post = Post.objects.get(id=id)
    devtoollist = []
    for list in lists:
      devtoollist.append(list.name)
    context = {"post":post, "devtools":devtoollist}
    return render(request, template_name="posts/ideaupdate.html", context=context)

def ideadelete(request, id):
  if request.method == "POST":
    Post.objects.filter(id=id).delete()
    return redirect("/")

def devtoollist(request):
  lists = Devtool.objects.all()
  context = {"lists":lists}
  return render(request, template_name="posts/devtoollist.html", context=context)

def devtoolregister(request):
  if request.method == "POST":
    name = request.POST["name"]
    kind = request.POST["kind"]
    content = request.POST["content"]

    Devtool.objects.create(name=name, kind=kind, content=content)
    return redirect(f"/devtoollist")

  context={}
  return render(request, template_name="posts/devtoolregister.html", context=context)

def devtooldetail(request, id):
  list = Devtool.objects.get(id=id)
  posts = Post.objects.all()
  context = {
    "list":list,
    "posts":posts
    }
  return render(request, template_name="posts/devtooldetail.html", context=context)

def devtoolupdate(request, id):
  if request.method == "POST":
    name = request.POST["name"]
    kind = request.POST["kind"]
    content = request.POST["content"]

    Devtool.objects.filter(id=id).update(name=name, kind=kind, content=content)
    return redirect(f"/devtooldetail/{id}")

  elif request.method == "GET":
    list = Devtool.objects.get(id=id)
    context = {"list":list}
    return render(request, template_name="posts/devtoolupdate.html", context=context)

def devtooldelete(request, id):
  if request.method == "POST":
    Devtool.objects.filter(id=id).delete()
    return redirect(f"/devtoollist")
