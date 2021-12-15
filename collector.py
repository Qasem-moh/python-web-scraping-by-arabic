import requests
from bs4 import BeautifulSoup

url = ''

req = requests.get(url).text

s = BeautifulSoup(req, 'html.parser')

collector = s.find_all(class_='')
print(collector)