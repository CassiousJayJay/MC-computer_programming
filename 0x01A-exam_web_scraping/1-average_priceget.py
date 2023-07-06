from bs4 import BeautifulSoup
import urllib.request

price = ['$10', '$15']
def get_average_price():
    total = 0
    for i in price:
        convert = i.replace('$', '')
        numHld = int(convert)
        total = total + numHld

        avg = total/len(price)
        print(str(avg))






        