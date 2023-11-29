import bs4
import requests

main_url = ''

url_5ka = 'https://5ka.ru/special_offers'

url_remi = 'https://remi.ru/news/'

url_samberi = 'https://www.samberi.com/actions'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0'}

excel_data = [['Наименование', 'Цена', 'Ссылка', 'Картинка']]

def get_soup(url):
    res = requests.get(url, headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')

categories_page = get_soup(url_5ka)
categories = categories_page.findAll('div', class= 'product-card item' )

for cat in categories:
    subcategories_page = get_soup(url_5ka + cat['href'])
    subcategories = subcategories_page.findAll('div', class= 'product-card item' )
    for subcat in subcategories:
        promotion_page = get_soup(url_5ka + subcat['href'])
        pomotions = promotion_page.findAll('div', class='')
        for promotion in promotions:
            title = promotion.find('a')

