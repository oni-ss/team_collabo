from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost

def home(request):
    blog = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    post = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blog, 'posts': post})

def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'details':detail})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('home')

def create(request):
    if request.method =='POST': 
        form = BlogPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:   
        form = BlogPost()
        return render(request,'create.html',{'form':form})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)

    if request.method == 'POST':
        form = BlogPost(request.POST, request.FILES, instance = blog)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = BlogPost(instance = blog)
        return render(request, 'create.html', {'form':form})