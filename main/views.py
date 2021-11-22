from django.shortcuts import render
from bs4 import BeautifulSoup#for the search functionnality
import requests
# Create your views here.
def home(request):
    return render(request, 'index.html')

def search(request):
    search= request.POST.get('q')
    print(search)
    stuff_frontend={"search":search,}
    return render(request, 'search.html', stuff_frontend)
