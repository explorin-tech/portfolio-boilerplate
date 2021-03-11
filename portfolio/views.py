from django.shortcuts import render

def home_page(request):
    return render(request, 'portfolio_home.html')

def website(request):
    return render(request, 'website.html')

def calculator(request):
    return render(request, 'calculator.html')

def loginpage(request):
    return render(request, 'loginpage.html')

def sql(request):
    return render(request, 'sql.html')
