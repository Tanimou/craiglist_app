from django.shortcuts import render
from bs4 import BeautifulSoup#for the search functionnality
import requests
from requests.compat import quote_plus
from .models import Search
# Create your views here.

BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/?query={}'#we put curly brack to dynamize the search result. 
                                                                          #We'll use the format function to associate the query part with the search results
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    return render(request, 'index.html')

def search(request):
    search= request.POST.get('q')
    Search.objects.create(search=search)
   # print(search)
    #print(quote_plus(search))
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))#this will concatenate the base craigslist url with the search results 
   # print(final_url)
    response=requests.get(final_url)#see python_tutorial/web scrapping for more informations
  #  print(response)

    data=response.text
    #print(data)


    soup = BeautifulSoup(data, features='html.parser')
    post_listings = soup.find_all('li', {'class': 'result-row'})
    #print(post_listings)
    final_postings = []

    for post in post_listings:
        post_title = post.find(class_="result-title").text
        post_url = post.find("a").get("href")

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find( class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
           # print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_postings.append( (post_title, post_url, post_price, post_image_url))
   # post_titles=soup.find_all("a",{"class":"result-title"})#will find all <a class="result-title">...</a> and return a list
   #print(post_titles[0].text)#will picks out everything between the tags, similar to get_text() function
   # print(post_titles[0].get("href"))#will get the link


    stuff_frontend={
        "search":search,
        "final_postings":final_postings,
        }

    return render(request, 'search.html', stuff_frontend)
