from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from django.contrib import messages

from .models import Blog, Category
from .forms import BlogAddForm


def blog_list_view(request):
    """
    listing out the all the available blogs
    :param request:
    :return:
    """
    query_param = request.GET.get('category')
    search_query = request.GET.get('q')
    if query_param:
        category = Category.objects.get(name=query_param)
        blog_lists = Blog.objects.filter(category=category.id, is_published=True)
    elif search_query:
        blog_lists = Blog.objects.filter(title__icontains=search_query, is_published=True)
    else:
        blog_lists = Blog.objects.filter(is_published=True)

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
    """
    viewing the detail about the specific blog
    :param request:
    :param slug:
    :return:
    """
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blog_detail.html', context=context)


class BlogAddView(LoginRequiredMixin, CreateView):
    """
    allowing users to post their own blog
    """
    form_class = BlogAddForm
    template_name ='blog/blog_add.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect('user:user-profile')


class BlogEditView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog/blog_edit.html'
    fields = ['title', 'description', 'meta_description', 'featured_image', 'image_url', 'category', 'tags']

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Blog Successfully Edited!!!")
        return super().form_valid(form)

    def get_success_url(self):
        url = '{}'.format(self.kwargs['pk'])
        return url