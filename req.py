import requests

url="http://testphp.vulnweb.com/index.php"

req=requests.get(url).text

f=open("page.html","w")

f.write(req)

f.close()

print(req)