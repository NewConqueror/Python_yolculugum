import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

liste = soup.find_all("li",{"class":"column"})

for li in liste:
    ad = li.div.a.h3.text.strip()
    link = li.div.a.get("href")
    
    fiyat = li.find("div",{"class":"proDetail"}).find("span").text

    print(f"ad: {ad} link: {link} fiyat: {fiyat}")