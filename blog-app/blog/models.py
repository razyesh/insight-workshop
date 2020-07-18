from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


def handle_featured_image(instance, filename):
    return "blog_{0}/{1}".format(instance.author.id, filename)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    author = models.ForeignKey(User, related_name='user_blog', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    description = models.TextField()
    meta_description = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to=handle_featured_image)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='blog_category')
    tags = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog List'
        verbose_name_plural = 'Blog Lists'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
