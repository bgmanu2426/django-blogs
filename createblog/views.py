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
            form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('ViweBlog')
    else:
        form = BlogForm()
    return render(request, 'blogform.html', {'form': form})


def editBlog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('ViweBlog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogform.html', {'form': form})


def deleteBlog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('ViweBlog')
    return render(request, 'deleteblog.html', {'blog': blog})

def getBlog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog.html', {'blog': blog})
