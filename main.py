from selenium import webdriver
from bs4 import BeautifulSoup
import json

driver = webdriver.Chrome()


url = "https://letterboxd.com/films/ajax/country/japan/by/release-earliest/page/"   # put here ur url


def getlinks(url):
    driver.get(url)
    driver.implicitly_wait(25)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    films = soup.find_all('li', class_='listitem poster-container')
    for film in films:
        film_div = film.find('div')
        if film_div:
            film_link = film_div['data-target-link']
            film_links.append('https://letterboxd.com' + film_link)
        else:
            print('not found')


film_links = []


def updt():
    curpage = 1
    while len(film_links) < 41500:    # put here ur num
        getlinks(url + str(curpage))
        curpage += 1
    with open('film_links_full.json', 'w', encoding='utf-8') as output_file:
        json.dump(film_links, output_file, indent=4, ensure_ascii=False)


updt()

driver.quit()
