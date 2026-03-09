from django.db import models
from django.utils.text import slugify

class BlogTag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name
    
class BlogCategory(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Blog categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(models.Model):

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts"
    )
    tags = models.ManyToManyField(
        BlogTag,
        blank=True,
        related_name="posts"
    )

    title = models.CharField(max_length=180)

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True
    )

    summary = models.CharField(
        max_length=255,
        blank=True
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to="blogs/",
        blank=True
    )

    is_published = models.BooleanField(
        default=True
    )

    published_at = models.DateTimeField(
        null=True,
        blank=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
