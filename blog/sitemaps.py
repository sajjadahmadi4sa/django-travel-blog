from django.contrib.sitemaps import Sitemap
from blog.models import Post


class BlogSitemaps(Sitemap):

    priority = 0.5
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date

    def get_urls(self, page=1, site=None, protocol=None):
        urls = super().get_urls(
            page=page,
            site=site,
            protocol='https',
        )

        for item in urls:
            item['location'] = item['location'].replace(
                'https://127.0.0.1:8000',
                'https://travel-blog.ir'
            )

        return urls