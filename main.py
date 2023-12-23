import bs4
import requests
import xlsxwriter

import openpyxl
from openpyxl import load_workbook

from flask import Flask, render_template

main_url = ''
url_5ka = 'https://5ka.ru/special_offers'
url_remi = 'https://remi.ru/news/'
url_samberi = 'https://www.samberi.com/actions'
url_sber_ashan = 'https://sbermarket.ru/auchan/c/priedlozhieniia'

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0'}

excel_data = [['Наименование', 'Цена', 'Дата', 'Картинка']]
excel_data_5ka = [['Наименование', 'Цена', 'Дата', 'Картинка']]
excel_data_SberAshan = [['Наименование', 'Цена', 'Дата']]

def get_soup_SberAshan(url_sber_ashan):
    res = requests.get(url, headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')

    promotions = url_sber_ashan.findAll('li', class_='Carousel_slide_qXWRh')
    for promotion in promotions:
        itemname = promotion.find('h3', class_='ProductCard_title__iNsaD').find(text = True).strip()
        itemprice = promotion.find('div', class_='ProductCardPrice_price__Kv7Q7 ProductCardPrice_accent__GwwRX').find(text = True).strip()
        itemdateend = promotion.find('span')['PromoBadge_info__GWtw9'].strip()
        excel_data.append([itemname, itemprice, itemdateend])

    with xlsxwriter.workbook('promotions_sberashan.xlsx') as workbook:
        workcheet = workbook.add_worksheet()
        for row_num, info in enumerate(excel_data):
            workcheet.write_row(row_num, info)


def test_excel():
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet['A1'] = 'Привет, мир!'
    workbook.save('example_test.xlsx')
    loaded_workbook = load_workbook('example.xlsx')
    loaded_sheet = loaded_workbook.active

    print(loaded_sheet['A1'].value)


