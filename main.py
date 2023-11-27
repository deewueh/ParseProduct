import bs4
import requests

def get_soup(url):
    res = requests.get(url, headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')


