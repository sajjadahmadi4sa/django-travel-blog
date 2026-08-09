from django.shortcuts import render
from blog.models import Post , Category
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

def blog_view (request,cid=None,author_username=None):
    posts = Post.objects.filter(status=1)
    if cid :
        posts = posts.filter(category__id=cid)
    if author_username :
        posts = posts.filter(author__username=author_username)
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts}
    return render(request,'blog/blog_home.html',context)

def blog_single_view (request,pid):
    post = get_object_or_404(Post, pk=pid, status=True)
    context = {'post':post}
    return render(request,'blog/blog_single.html' , context)

def blog_search(request):
    posts = Post.objects.filter(status=True)
    q = request.GET.get('q', '').strip()
    if q:
        posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))
    context = {'posts': posts,'q': q,}
    return render(request, 'blog/blog_search.html', context)





