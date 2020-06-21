from django.contrib import admin
from . models import banner, product, siteInfo

admin.site.register(banner)

admin.site.register(siteInfo)

class ProductPost(admin.ModelAdmin):
    list_display = ('id', 'productName', 'productImg', 'productImg2', 'productImg3','productCategories', 'productPrice','productOffer','featuredproduct','OfferPercent')
    list_filter = ("productCategories",)
    search_fields = ['productName', 'productCategories','productPrice']
admin.site.register(product, ProductPost)

