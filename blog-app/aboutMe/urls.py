from django.urls import path
from .views import home

app_name = 'aboutMe'
urlpatterns = [
    path('', home, name='home')
]