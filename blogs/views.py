from django.shortcuts import render

from blogs.models import BlogPost


def blog_list(request):

    blogs = BlogPost.objects.filter(is_published=True)

    return render(
        request,
        "blogs/blog.html",
        {"blogs": blogs}
    )


def blog_detail(request):
    return render(request, "blogs/single.html")
