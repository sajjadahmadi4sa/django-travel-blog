from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from blog.sitemaps import BlogSitemaps


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('website.urls')),

    path('blog/', include('blog.urls')),

    path('accounts/', include('accounts.urls')),

    path('captcha/', include('captcha.urls')),

    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': {'blog': BlogSitemaps}},
    ),

    path('robots.txt', include('robots.urls')),
]


if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )