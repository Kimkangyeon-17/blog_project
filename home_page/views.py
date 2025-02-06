from django.shortcuts import render

def landing(request):
    return render(request, 'home_page/landing.html')