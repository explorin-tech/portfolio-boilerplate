from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page')

def website(request):
    return render(request, 'website')

def calculator(request):
    return render(request, 'calculator')

def login_page(request):
    return render(request, 'loginpage')

def sql(request):
    return render(request, 'sql')
