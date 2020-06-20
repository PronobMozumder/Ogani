from django.urls import path, include
from . import views

app_name ="eco"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.shopdetails, name="shopdetails"),
    path('shopgrid', views.shopgrid, name="shopgrid"),
    path('shopingcart', views.shopingcart, name="shopingcart"),
    path('checkout', views.checkout, name="checkout"),
    path('<str:categories>/<int:id>', views.blogdetails, name="blogdetails"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    path('base', views.base, name ="base"),
]
