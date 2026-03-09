from django.shortcuts import render

from blogs.models import BlogPost


from .models import BlogPost, BlogCategory, BlogTag


def blog_list(request):

    blogs = BlogPost.objects.filter(is_published=True)

    categories = BlogCategory.objects.all()

    tags = BlogTag.objects.all()

    return render(
        request,
        "blogs/blog.html",
        {
            "blogs": blogs,
            "categories": categories,
            "tags": tags
        }
    )


def blog_detail(request):
    return render(request, "blogs/single.html")
