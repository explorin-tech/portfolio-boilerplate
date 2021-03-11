from django.shortcuts import render

def home_page(request):
    return render(request, 'insta_home.html')
