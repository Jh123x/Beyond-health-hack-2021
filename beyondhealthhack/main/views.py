from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """Home page for the website"""
    return render(request, 'main_page.html')