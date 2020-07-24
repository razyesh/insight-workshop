from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from blog.models import Blog

User = get_user_model()


class UserProfileView(LoginRequiredMixin, View):
    """
    viewing user profile
    """
    login_url = 'authentication:login-user'
    redirect_field_name = 'next'

    def get(self, request):
        blogs = Blog.objects.filter(author=request.user)
        context = {
            'blogs': blogs
        }
        return render(request, 'user/profile.html', context=context)


def upload_profile(request):
    if request.method == 'POST':
        image = request.FILES['profile-img']
        user = request.user
        user.image = image
        user.save()
        return redirect('user:user-profile')
