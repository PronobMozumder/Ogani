from django.shortcuts import render, get_object_or_404
from . models import banner, product, siteInfo, blogPost
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def base(request):
    info = siteInfo.objects.get(id=1)
    Products = product.objects.all()
    herro = None
    return render(request, 'base.html', {'Products':Products, 'herro':herro, 'info': info})

def index(request):
    info = siteInfo.objects.get(id=1)
    Products = product.objects.all()
    Banner = banner.objects.get(id=1)
    herro = 'hero-normal'
    return render(request, 'index.html' , {'banner':Banner, 'Products':Products, 'herro':herro, 'info': info})

def shopdetails(request, id):
    Products = product.objects.all()
    post = get_object_or_404(product, id = id)
    info = siteInfo.objects.get(id=1)
    herro = 'hero-normal'
    return render(request, 'shop-details.html', {'herro':herro, 'post':post, 'Products':Products, 'info': info})

def shopgrid(request):
    info = siteInfo.objects.get(id=1)

    Products = product.objects.all()
    paginator = Paginator(Products, 6)
    
    page = request.GET.get('page')
    
    try:
        Product = paginator.get_page(page)
    except PageNotAnInteger:
        Product = paginator.get_page(1)
    except EmptyPage:
        Product = paginator.get_page(paginator.num_pages)

    herro = 'hero-normal'
    return render(request, 'shop-grid.html', {'page': page,'Products':Product, 'herro':herro, 'info': info})

def shopingcart(request):
    info = siteInfo.objects.get(id=1)
    Products = product.objects.all()
    herro = 'hero-normal'
    return render(request, 'shoping-cart.html', {'Products':Products,'herro':herro, 'info': info})

def checkout(request):
    info = siteInfo.objects.get(id=1)
    Products = product.objects.all()
    herro = 'hero-normal'
    return render(request, 'checkout.html', {'Products':Products,'herro':herro, 'info': info})

def blogdetails(request, categories, id):
    blogs = blogPost.objects.all()
    BPost = get_object_or_404(blogPost, categories= categories, id = id)
    info = siteInfo.objects.get(id=1)
    Products = product.objects.all()
    herro = 'hero-normal'
    return render(request, 'blog-details.html', {'Products':Products,'herro':herro, 'BPost':BPost, 'blogs':blogs, 'info': info})

def blog(request):
    info = siteInfo.objects.get(id=1)
    Products = product.objects.all()

    blogs = blogPost.objects.all()
    paginator = Paginator(blogs, 4)
    
    page = request.GET.get('page')
    
    try:
        Blogs = paginator.get_page(page)
    except PageNotAnInteger:
        Blogs = paginator.get_page(1)
    except EmptyPage:
        Blogs = paginator.get_page(paginator.num_pages)

    herro = 'hero-normal'
    return render(request, 'blog.html', {'Products': Products , 'page': page, 'BlogsPost':Blogs, 'herro':herro, 'info': info})
    

def contact(request):
    info = siteInfo.objects.get(id=1)
    Products = product.objects.all()
    herro = 'hero-normal'
    return render(request, 'contact.html', {'Products':Products,'herro':herro, 'info': info})

