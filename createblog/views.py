from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.


def ViweBlog(request):
    blogs = Blog.objects.all().order_by('-date_posted')
    return render(request, 'index.html', {'blogs': blogs})


def CreateBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('allBlogs')
    else:
        form = BlogForm()
    return render(request, 'blogform.html', {'form': form})


def EditBlog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, author=request.user) # This line is the only difference between this function and the CreateBlog function.
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('allBlogs')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogform.html', {'form': form})


def DeleteBlog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('allBlogs')
    return render(request, 'deleteblog.html', {'blog': blog})

def GetBlog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog.html', {'blog': blog})
