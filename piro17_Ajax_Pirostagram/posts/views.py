from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
  comments = Comment.objects.all()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    print(form)
    if form.is_valid():
      form.save()
      return redirect('posts:home')
    else:
      context = {
          'comments': comments,
          'form': form,
      }
      return render(request, template_name='posts/home.html', context=context)
  
  else:
    form = CommentForm()
    context = {
        'comments': comments,
        'form': form,
    }
    return render(request, template_name='posts/home.html', context=context)


@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body) 
    comment_id = req['id'] 
    comment = Comment.objects.get(id = comment_id)

    if comment.like == True: #좋아요가 눌러져있으면
        comment.like = False
    else: #좋아요가 안눌러져있으면
        comment.like = True
    comment.save()

    return JsonResponse({'id': comment_id})

@csrf_exempt
def delete(request):
    req = json.loads(request.body)
    comment_id = req['id']
    Comment.objects.filter(id=comment_id).delete()

    return JsonResponse({ 'id': comment_id })