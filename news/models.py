from django.db import models
from django.utils.text import slugify
from tags.models import Tag
from categories.models import Category


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    tags = models.ManyToManyField(Tag, related_name='news')
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    view_count = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

