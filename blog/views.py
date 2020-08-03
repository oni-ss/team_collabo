from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogPost

def home(request):
    blog = Blog.objects
    blog_list = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blog, 'posts': posts})

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':detail})

def create(request):
    if request.method =='POST': 
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else: 
        form = BlogPost()
        return render(request,'create.html',{'form':form})

def update(request, blog_id):
    blogs = get_object_or_404(Blog, pk = blog_id)

    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES, instance = blogs)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = BlogPost(instance = blogs)
        return render(request, 'create.html', {'form':form})


def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')