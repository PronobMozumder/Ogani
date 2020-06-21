from django.shortcuts import render, get_object_or_404
from . models import blogPost
from lookup . models import banner, product, siteInfo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
 