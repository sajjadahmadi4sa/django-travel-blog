from django.contrib import admin
from blog.models import Post , Category



class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    search_fields = ['title','content']
    list_filter = ('status','created_date', 'published_date','author',)
    list_display = ('title','status','created_date','updated_date','published_date','counted_view','author',)
    list_editable = ('status',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
  

# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)