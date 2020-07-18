from django.shortcuts import render

from .models import Blog, Category


def blog_list_view(request):
    query_param = request.GET.get('category')
    search_query = request.GET.get('q')
    if query_param:
        category = Category.objects.get(name=query_param)
        blog_lists = Blog.objects.filter(category=category.id)
    elif search_query:
        blog_lists = Blog.objects.filter(title__icontains=search_query)
    else:
        blog_lists = Blog.objects.all()

    if blog_lists:
        context = {
            'blogs': blog_lists
        }
    else:
        context = {
            'message': f"No Results Found"
        }
    return render(request, 'blog/blog_list.html', context=context)


def blog_detail_view(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context=context)
