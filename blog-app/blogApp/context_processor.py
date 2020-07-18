from blog.models import Category
from blog.models import Blog


def blog_categories_list(request):
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    return {
        'categories' : categories,
        'blogs':blogs
    }
