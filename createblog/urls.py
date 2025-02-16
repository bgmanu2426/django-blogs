from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViweBlog, name='allBlogs'),
    path('/create/', views.CreateBlog, name='createBlog'),
    path('/edit/<int:blog_id>/', views.EditBlog, name='editBlog'),
    path('/delete/<int:blog_id>/', views.DeleteBlog, name='deleteBlog'),
    path('/blog/<int:blog_id>/', views.GetBlog, name='getBlog'),
]
