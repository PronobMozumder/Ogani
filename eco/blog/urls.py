from django.urls import path, include
from . import views

app_name ="blog"
urlpatterns = [
    path('<str:categories>/<int:id>', views.blogdetails, name="blogdetails"),
    path('blog', views.blog, name="blog"),
]
