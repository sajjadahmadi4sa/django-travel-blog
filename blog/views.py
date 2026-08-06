from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404

def blog_view (request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog_home.html',context)

def blog_single_view (request,pid):
    post = get_object_or_404(Post, pk=pid, status=True)
    context = {'post':post}
    return render(request,'blog/blog_single.html' , context)
# Create your views here.
