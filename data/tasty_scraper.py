import requests
from bs4 import BeautifulSoup as soup  

#Make url request for url
get = requests.get('https://tasty.co/compilation/44-easy-3-ingredient-recipes')
c = get.content
page = soup(c,'html.parser')

def get_items(page):
    '''Take in the Tasty.co page and return dict
       of food item urls'''
    #grab container for food items
    feed_items = page.find('div',{'class':'feed__items'})

    #get list of items
    item_list = feed_items.findAll('a',{'class':'feed-item'})

    #dictionary comprehension for recipes and their urls 
    item_urls = {item.find('div',{'class':'feed-item__title'}).text:item['href'] for item in item_list} 

    return item_urls

print(get_items(page))







