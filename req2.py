import requests
from bs4 import BeautifulSoup

url = "http://testphp.vulnweb.com/index.php"

req = requests.get(url).text

soup = BeautifulSoup(req, 'html.parser')

# find = soup.find("h2")

# find_all= soup.find_all("a")

# for link in find_all:
#     print(link)


# print(find.text)

# print(find.prettify())

####################By ID##################

byid = soup.find(id='pageName')
print(byid)

byid2 = soup.find("h2", id='pageName')
print(byid2)

all_by_id = soup.find_all(id='pageName')
print(all_by_id)

all_by_id2 = soup.find_all("h2", id='pageName')
print(all_by_id2)

####################By class##################

byid = soup.find(class_='pageName')
print(byid)

byid2 = soup.find("h2", class_='pageName')
print(byid2)

all_by_id = soup.find_all(class_='pageName')
print(all_by_id)

all_by_id2 = soup.find_all("h2", class_='pageName')
print(all_by_id2)
