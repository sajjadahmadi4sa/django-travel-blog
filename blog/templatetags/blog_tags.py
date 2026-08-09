from django import template
from blog.models import Post , Category
register = template.Library()


@register.inclusion_tag('blog/recent_posts.html')
def recent_posts ():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts':posts}

@register.inclusion_tag('blog/blog_post_category.html')
def postcategories ():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for category in categories:
        cat_dict[category] = posts.filter(category=category).count()
    return {'categories': cat_dict}