from ast import Return
from django.shortcuts import redirect, render
from .models import Post

def home(request):
	posts = Post.objects.all()
	context = {"posts": posts}
	return render(request, template_name="posts/home.html", context=context)

def create(request):
	if request.method == 'POST':
		title = request.POST["title"]
		release_year = request.POST["release_year"]
		genre = request.POST["genre"]
		star_rating = request.POST["star_rating"]
		running_time = request.POST["running_time"]
		content = request.POST["content"]
		director = request.POST["director"]
		lead_role = request.POST["lead_role"]

		Post.objects.create(title=title, release_year=release_year, genre=genre, star_rating=star_rating,
		running_time=running_time, content=content, director=director, lead_role=lead_role)

		return redirect("/")
	
	context = {}
	return render(request, template_name="posts/create.html", context=context)

def detail(request, id):
	post = Post.objects.get(id=id)
	context = {"post":post}
	return render(request, template_name="posts/detail.html", context=context)

def update(request, id):
	if request.method == 'POST':
		title = request.POST["title"]
		release_year = request.POST["release_year"]
		genre = request.POST["genre"]
		star_rating = request.POST["star_rating"]
		running_time = request.POST["running_time"]
		content = request.POST["content"]
		director = request.POST["director"]
		lead_role = request.POST["lead_role"]

		Post.objects.filter(id=id).update(title=title, release_year=release_year, genre=genre, star_rating=star_rating,
		running_time=running_time, content=content, director=director, lead_role=lead_role)

		return redirect(f"/post/{id}")
	
	elif request.method == 'GET':
		post = Post.objects.get(id=id)
		context = {"post":post}
		return render(request, template_name="posts/update.html", context=context) 

def delete(request, id):
  if request.method == "POST":
    Post.objects.filter(id = id).delete()
    return redirect("/")