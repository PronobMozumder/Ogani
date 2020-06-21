from django.contrib import admin
from . models import blogPost


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author','blogImg', 'status','created_on','content')
    list_filter = ("categories",)
    search_fields = ['title', 'content']
    
admin.site.register(blogPost, PostAdmin)
