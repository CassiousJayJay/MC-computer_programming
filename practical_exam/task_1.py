import requests
from bs4 import BeautifulSoup


page = requests.get('https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.html')

soup = BeautifulSoup(page.text, 'html.parser')
print(soup)

#artist_name_list = soup.find(class_= 'BodyText')

#artist_name_list_items = artist_name_list.find_all('a')

#for artist_name in artist_name_list_items:
    #print(artist_name.prettify())