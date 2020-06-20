from django.contrib import admin
from . models import banner, product, siteInfo, blogPost

admin.site.register(banner)

admin.site.register(siteInfo)

class ProductPost(admin.ModelAdmin):
    list_display = ('id', 'productName', 'productImg', 'productImg2', 'productImg3','productCategories', 'productPrice','productOffer','featuredproduct','OfferPercent')
    list_filter = ("productCategories",)
    search_fields = ['productName', 'productCategories','productPrice']
admin.site.register(product, ProductPost)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author','blogImg', 'status','created_on','content')
    list_filter = ("categories",)
    search_fields = ['title', 'content']
    
admin.site.register(blogPost, PostAdmin)
