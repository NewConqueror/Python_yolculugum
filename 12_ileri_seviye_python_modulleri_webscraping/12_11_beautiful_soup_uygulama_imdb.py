import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"

html = requests.get(url).content  # content ile html dokümanına çevirdik komple

soup = BeautifulSoup(html,"html.parser")

liste = soup.find("div",{"class":"lister-list"}).find_all("tr",limit=1) #listerlist i bul içinden 50 tane tr yi al bir listeye

sayac =1

for tr in liste:

    baslik = tr.find("td",{"class":"titleColumn"}).find("a").text

    yil = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")

    puan = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text

    print(f"{sayac}- film: {baslik.ljust(50)} yıl: {yil} değerlendirme: {puan}")
    sayac+=1