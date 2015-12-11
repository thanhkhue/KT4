from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog

def index(request):
    return render(request, 'blog/index.html')

def detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Blog.DoesNotExist:
        raise Http404("Blog does not exist")
    return render(request, 'blog/detail.html', {'blog': blog})

def blog(request):
    latest_post_list = Blog.objects.order_by('-publication_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/blog.html', context)