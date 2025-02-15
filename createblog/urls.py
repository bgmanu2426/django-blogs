from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViweBlog, name='allBlogs'),
    path('/create/', views.CreateBlog, name='createBlog'),
    path('/edit/<int:blog_id>/', views.editBlog, name='editBlog'),
    path('/delete/<int:blog_id>/', views.deleteBlog, name='deleteBlog'),
    path('/blog/<int:blog_id>/', views.getBlog, name='getBlog'),
]
