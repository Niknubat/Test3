# Сделал только до парсера, страницу не спарсил

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.onlyoffice.com/en/")
driver.find_element_by_id("navitem_about").click()
driver.find_element_by_id("navitem_about_about").click()

# Все что ниже, не работает
# driver.get('https://www.onlyoffice.com/en/about.aspx') # Получение HTML-содержимого
# import requests # pip install requests
# def get_html(url):
#     r = requests.get('https://www.onlyoffice.com/en/about.aspx')    # Получаем метод Response
#     r.encoding = 'utf8'      # У меня были проблемы с кодировкой, я задал в ручную
#     return r.text            # Вернем данные объекта text
#
# from bs4 import BeautifulSoup
#
# html = BS(r.content, 'html/parser')
# for el in html.select('.owl-item cloned active'):
#     title = el.select('.owl-item cloned active > a')
#     print(title[0].text)