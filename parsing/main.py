'''
1. Получить HTML - код страницы
2. Получить блок с товарами в HTML - коде 
3. Получить данные из блока
4. Сохранить полученные данные в файл (json, csv, txt)
'''
import requests 
from bs4 import BeautifulSoup as BS 

Path = 'https://enter.kg/computers/noutbuki_bishkek'

def get_html(url): 
    html = requests.get(url)
    return (html.text)

def soup_html(html):
    soup = BS(html, 'lxml')
    return(soup)
 
def get_data(soup):
    data = soup.find_all('div',class_ = 'row')
    list_ = []
    for nout in data:
        title = (nout.find('span',class_ = 'prouct_name').text)
        img = ('https://enter.kg' + nout.find('img').get('src'))
        price = (nout.find('span', class_='price').text)
        list_.append({'title':title,'img':img, 'price':price})
    return list_
def get_total_page(url,count):
    html = requests.get(f'{url}/results,{count*100+1}-{count*100}') 
    return html.text

def get_last_page(url):
    html = get_html(url)
    soup = soup_html(html)
    last_page = soup.find('span',class_ = 'vm-page-counter').text[-2:]
    return last_page

def main(url): 
    count = 0
    last_page = get_last_page(url)
    while count < int(last_page):
        html = get_total_page(url,count)
        soup = soup_html(html)
        data = get_data(soup)
        print(f'спарсилась страница {count+1}')
        count+=1

main(Path)

# html = get_html(Path)
# soup = soup_html(html)
# get_data(soup)



'requests - модуль для отправки запросов на сайт'
'BS4 - форматирует html в более удобный вид и позваляет использовать методы .find, .find_all для поиска тегов'
'lxml - это парсер, который позволяет стягивать информацию с soup'

# find - метод, который позволяет найти первый попавшийся тег под каким-то классом
# fild_all - метод, который позволяет найти все теги под каким-то классом. Прилетает list с найденными тегами

# .get - мы получаем атрибуты тегов (href, src) 
 