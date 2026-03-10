from modeltranslation.translator import register, TranslationOptions
from .models import BlogPost, BlogCategory, BlogTag


@register(BlogPost)
class BlogPostTranslationOptions(TranslationOptions):
    fields = ("title", "summary", "content")


@register(BlogCategory)
class BlogCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(BlogTag)
class BlogTagTranslationOptions(TranslationOptions):
    fields = ("name",)