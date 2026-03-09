from django.contrib import admin
from .models import BlogCategory, BlogPost, BlogTag


admin.site.register(BlogPost)
admin.site.register(BlogCategory)
admin.site.register(BlogTag)