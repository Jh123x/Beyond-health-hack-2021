from django.http.response import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Blog

# Create your views here.
def index(request):
    """The main blog page"""
    page = request.GET.get('page', 1)
    if page <= 0:
        return HttpResponseNotFound("This page is not found")
    blog_posts = Blog.objects.filter(is_published=True).all()[page-1:page+9]
    return render(request, 'blog_list.html', {'blogs': blog_posts})


# Specific Blog page
def blog(request, id: int):
    """Renders the specific blog"""
    blog = get_object_or_404(Blog, pk=id)

    if not blog.is_published:
        return HttpResponseNotFound("This page is not found")

    if blog.has_trigger_warning and not request.user.is_authenticated:
        messages.info(request, "You need to login to view this post")
        return redirect('/blog')

    blog.views += 1
    blog.save()
    return render(request, 'blog.html', {'blog': blog})
