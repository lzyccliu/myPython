from django.contrib import admin
from blog.models import BlogsPost,BlogPostAdmin
# Register your models here.

class BlogPostAdmins(admin.ModelAdmin):
    #fields = ['text','title']           #改变内容编辑页的格式
    list_display=('text','date_added')

admin.site.register(BlogsPost)
admin.site.register(BlogPostAdmin,BlogPostAdmins)