from django.shortcuts import render
from blog.models import Post , Category , Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from taggit.models import Tag
from blog.forms import CommentForm
from django.contrib import messages



def blog_view (request,cid=None,author_username=None,tag_name=None):
    posts = Post.objects.filter(status=1)
    if cid :
        posts = posts.filter(category__id=cid)
    if author_username :
        posts = posts.filter(author__username=author_username)
    if tag_name:
        posts = posts.filter(tags__name__in=[tag_name])
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    tags = Tag.objects.all()
    context = {'posts':posts , 'tags': tags, }
    return render(request,'blog/blog_home.html',context)

def blog_single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=True)
    post.counted_view += 1
    post.save(update_fields=['counted_view'])
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posts = post
            comment.save()
            messages.add_message( request, messages.SUCCESS,'Your message was sent successfully!')
        else:
            messages.add_message(request,messages.ERROR,'Your message was not valid!')
    else:
        form = CommentForm()
    tags = post.tags.all()
    comments = Comment.objects.filter( posts=post, approved=True).order_by('-created_date')
    context = {'post': post,'tags': tags,'comments': comments,'form': form,}
    return render(request, 'blog/blog_single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=True)
    q = request.GET.get('q', '').strip()
    if q:
        posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))
    context = {'posts': posts,'q': q,}
    return render(request, 'blog/blog_search.html', context)





