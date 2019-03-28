#-*-coding:utf-8-*-

import requests, re
from bs4 import BeautifulSoup as bs


headers = {'accept':'*/*', 
           'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

url = 'https://finance.rambler.ru/currencies'

cod = []
nom = []
cur = []
cha = []
per = []
data = []

def main():

    session = requests.Session()
    request = session.get(url, headers=headers)
    soup = bs(request.content, 'html.parser')
    

    data = soup.find('div', class_='finance-currency-table__table')

    codes = data.find_all('div', class_=re.compile('.*--code.*'))
    nominals = data.find_all('div', class_=re.compile('.*--denomination.*'))
    currencies = data.find_all('div', class_=re.compile('.*--currency.*'))
    changes = data.find_all('div', class_=re.compile('.*--change.*'))
    percents = data.find_all('div', class_=re.compile('.*--percent.*'))

    for c in codes:
        code = c.text.replace('\n', '')
        cod.append(code)

    for n in nominals:
        nominal = n.text.replace('\n', '')
        nom.append(nominal)

    for c in currencies:
        currency = c.text.replace('\n', '')
        cur.append(currency)

    for c in changes:
        change = c.text.replace('\n', '')
        cha.append(change)

    for p in percents:
        percent = p.text.replace('\n', '')
        per.append(percent)

    data = list(zip(cod, nom, cur, cha, per))


    return data


main()