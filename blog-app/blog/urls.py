from django.urls import path
from .views import blog_list_view, blog_detail_view, BlogAddView, BlogEditView

app_name = 'blog'
urlpatterns = [
    path('', blog_list_view, name='blog-list'),
    path('detail/<slug:slug>', blog_detail_view, name='blog-detail'),
    path('add', BlogAddView.as_view(), name='blog-add'),
    path('edit/<int:pk>', BlogEditView.as_view(), name="blog-edit")
]