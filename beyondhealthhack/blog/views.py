from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .models import Blog

# Create your views here.
def index(request):
    """The main blog page"""
    page = request.GET.get('page', 1)
    if page <= 0:
        return HttpResponseNotFound("This page is not found")
    blog_posts = Blog.objects.all()[page-1:page+9]
    return HttpResponse(f"Blog posts: {', '.join(map(lambda x: x.__str__(), blog_posts))}")


# Specific Blog page
def blog(request, id: int):
    """Renders the specific blog"""
    blog = get_object_or_404(Blog, pk=id)
    blog.views += 1
    blog.save()
    return HttpResponse(f"This is blog {blog.id}\nTitle: {blog.title}\nViews: {blog.views}\nLikes: {blog.likes}\nContents: \n{blog.content}\n", {"blog": blog})


