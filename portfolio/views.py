from django.shortcuts import render

def home_page(request):
    return render(request, 'home_page.html')

def website(request):
    return render(request, 'website')

def calculator(request):
    return render(request, 'calculator')

def loginpage(request):
    return render(request, 'loginpage')

def sql(request):
    return render(request, 'sql')
