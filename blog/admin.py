from django.contrib import admin
from blog.models import Post , Category , Comment



class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['title','content']
    list_filter = ('status','created_date', 'published_date','author',)
    list_display = ('title','status','created_date','updated_date','published_date','counted_view','author',)
    list_editable = ('status',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '_empty_'
    list_display = ('name',)
    list_filter = ('name','approved','created_date',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)