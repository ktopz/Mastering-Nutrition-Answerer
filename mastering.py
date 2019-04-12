from googlesearch import search

input = input("Copy and paste question\n")

quoted_input = '"' + input + '"'

urls = []

for url in search(quoted_input, stop=2):
    urls.append(url)


from bs4 import BeautifulSoup
import requests


if('quizlet' in urls[0]):
    source = requests.get(urls[0]).text
    soup = BeautifulSoup(source, 'html5lib')
    div = soup.find('div', class_='SetPage-terms')
    divs = div.find_all('div', class_='SetPageTerm-content')
    for div in divs:
        if input in div.find('span', class_='TermText notranslate lang-en'):
            subdivs = div.find_all('span', class_='TermText notranslate lang-en')
            print(subdivs[1].text)

    #divs = soup.find('section',class_='UISection SetPageTerms-termsWrapper').find('div')
    #for div in divs:
    #    print(div)
