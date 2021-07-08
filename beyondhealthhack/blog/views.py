from django.contrib.auth import get_user
from django.http.response import HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Blog

# Create your views here.
def index(request):
    """The main blog page"""
    sort_dict = {
        'title': lambda x: x.title,
        'likes': lambda x: x.likes,
        'views': lambda x: x.views,
        'date': lambda x: x.date,
    }
    page = request.GET.get('page', 1)
    if page <= 0:
        return HttpResponseNotFound("This page is not found")
    blog_posts = Blog.objects.filter(is_published=True).all()[page-1:page+9]

    sort_key = request.GET.get('sort_by', None)
    reversed_key = request.GET.get('reversed', None)
    
    if sort_key is not None:
        t = sort_dict[sort_key]
        blog_posts = sorted(blog_posts, key=t, reverse=reversed_key is None)

    return render(request, 'blog_list.html', {'blogs': blog_posts})


# Specific Blog page
def blog(request, id: int):
    """Renders the specific blog"""
    blog = get_object_or_404(Blog, pk=id)

    if not blog.is_published:
        return HttpResponseNotFound("This page is not found")

    if not blog.is_public and not request.user.is_authenticated:
        messages.info(request, "You need to login to view this post")
        return redirect('/blog')

    blog.views += 1
    blog.save()
    return render(request, 'blog.html', {'blog': blog})


# Posting a blog
@login_required(redirect_field_name='login', login_url="/login")
def post_blog(request):
    """Page for posting a blog"""
    if request.method == "GET":
        return render(request, "post_blog.html")

    if request.method != "POST":
        return HttpResponseNotFound("Method not allowed")

    post_title = request.POST.get("title")
    post_body = request.POST.get("body")
    is_public = request.POST.get("is_public", False)
    user = get_user(request)

    blog = Blog(title=post_title, content=post_body, author=user.get_username(), is_public=bool(is_public))
    blog.save()

    messages.info(request, "Your blog will be visible once it is approved")
    return redirect(f"/blog/")