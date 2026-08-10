from django.contrib.syndication.views import Feed
from .models import Post


class LatestPostsFeed(Feed):
    title = "My Blog"
    link = "/blog/"
    description = "Latest posts from my blog"
    
    def items(self):
        return Post.objects.filter(status=True).order_by('-created_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    def item_link(self, item):
        return item.get_absolute_url()