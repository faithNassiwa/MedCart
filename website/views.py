from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'website/home.html')


def policy(request):
    return render(request, 'website/policy.html')