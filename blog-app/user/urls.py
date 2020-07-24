from django.urls import path
from .views import UserProfileView, upload_profile

app_name = 'user'

urlpatterns = [
    path('profile', UserProfileView.as_view(), name='user-profile'),
    path('upload/profile/image', upload_profile, name='upload-image')
]