import requests
from bs4 import BeautifulSoup

url = ''

req = requests.get(url).text

s = BeautifulSoup(req, 'html.parser')

collector = s.find_all(class_='')

for email in collector:
    print(email)
