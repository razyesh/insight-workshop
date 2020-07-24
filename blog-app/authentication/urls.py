from django.urls import path
from .views import login_user, logout_user, UserRegisterView, activate

app_name = 'authentication'
urlpatterns = [
    path('login', login_user, name='login-user'),
    path('logout', logout_user, name='logout-user'),
    path('register', UserRegisterView.as_view(), name='register-user'),
    path('activate/<uidb64>/<token>', activate, name='activate')
]