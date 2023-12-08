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

promotion_page_5ka = get_soup(url_5ka)

for cat in categories:
    promotion_page_5ka = get_soup(url_5ka + subcat['href'])
    pomotions = promotion_page_5ka.findAll('div', class_='product-card item')
    for promotion in promotions:
        itemname = promotion.find('div', class_='item-name').find(text = True).strip()
        itemprice = promotion.find('span', class_='from').find(text = True).strip()
        itemdateend = promotion.find('div')['item-date'].strip()
        itemimg = promotion.find('div')
        data.append([itemname, itemprice, itemdateend, itemimg])



