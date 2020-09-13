from django.shortcuts import render
from .models import Post

def blog_view(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'blog.html', {'posts':posts})

def create_post_view(request):
    if request.POST.get('action') == 'create-post':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Post.objects.create(
            title=title,
            description=description,
            image=image
        )

    return render(request, 'create-post.html')