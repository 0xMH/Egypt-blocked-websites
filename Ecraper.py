import requests
from bs4 import BeautifulSoup
from urllib.request import urlsplit

general = 'https://afteegypt.org/blocked-websites-list?lang=en'
afteegypt = requests.get(general)
parse = BeautifulSoup(afteegypt.content, "html5lib")

blocked_websties = []

for table in parse.find_all('table'):

    for tr in table.findAll('tr', attrs={'style': 'height: 26px;'}):
        for anchor in tr.findAll('a'):
            url = urlsplit(anchor.get('href')).netloc
            blocked_websties.append(url)

    # Second half of the tables
    for td1 in table.findAll('td', attrs={'style':'background-color: #faf2f2; text-align: center; height: 26px; width: 214px;', 'colspan':'2'}):
        v = td1.renderContents()
        for x in str(v.decode('utf-8')).replace('<br/>', '').split():
            blocked_websties.append(x)

    # First half of the tables
    for td2 in table.findAll('td', attrs={'style':'background-color: #faf2f2; width: 180px; height: 26px; text-align: center;', 'colspan':'2'}):
        v = td2.renderContents()
        for x in str(v.decode('utf-8')).replace('<br/>', '').split():
            blocked_websties.append(x)

print(blocked_websties)
with open('blocked-websites.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(blocked_websties))
