#-*-coding:utf-8-*-

import requests, re
from bs4 import BeautifulSoup as bs


headers = {'accept':'*/*', 
           'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

ban = ['Код', 'Номинал', 'Валюта', 'Изменения', '%']

url = 'https://finance.rambler.ru/currencies'

cod = []
nom = []
cur = []
val = []
cha = []
per = []
data = []

def main():

    session = requests.Session()
    request = session.get(url, headers=headers)
    soup = bs(request.content, 'html.parser')
    

    data = soup.find('div', class_='finance-currency-table__table')

    codes = data.find_all('div', class_=re.compile('.*--code.*'))[0:]
    nominals = data.find_all('div', class_=re.compile('.*--denomination.*'))[0:]
    currencies = data.find_all('div', class_=re.compile('.*--currency.*'))[0:]
    values = data.find_all('div', class_=re.compile('.*--value.*'))[0:]
    changes = data.find_all('div', class_=re.compile('.*--change.*'))[0:]
    percents = data.find_all('div', class_=re.compile('.*--percent.*'))[0:]

    for c in codes:
        if not c in ban:
            code = c.text.replace('\n', '')
            cod.append(code)

    for n in nominals:
        if not n in ban:
            nominal = n.text.replace('\n', '')
            nom.append(nominal)

    for c in currencies:
        if not c in ban:
            currency = c.text.replace('\n', '')
            cur.append(currency)

    for v in values:
        if not v in ban:
            value = v.text.replace('\n', '')
            val.append(value)

    for c in changes:
        if not c in ban:
            change = c.text.replace('\n', '')
            cha.append(change)

    for p in percents:
        if not p in ban:
            percent = p.text.replace('\n', '')        
            per.append(percent)

    data = list(zip(cod, nom, cur, val, cha, per))[1:]
    
    return data

