from django.shortcuts import render

# Create your views here.


def home(request):
    page_title = 'About Me'
    return render(request, 'aboutMe/home.html', {'page_title':page_title})