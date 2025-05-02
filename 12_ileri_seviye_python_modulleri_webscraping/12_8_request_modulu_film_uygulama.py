
import requests
import json

class MoiveDb:

    def __init__(self):
        
        self.apiurl = "https://api.themoviedb.org/3"
        self.apikey = "e35e8781f0006a53ec2bf0ee54b7d04e"

    def popüler(self):

        cevap = requests.get(f"{self.apiurl}/movie/popular?api_key={self.apikey}&language=en-US&page=1")
        
        return cevap.json()  # pythonda kullanabileceğimiz yapıya çevirdik
    
    def ara(self,kelime):
        
        cevap = requests.get(f"{self.apiurl}/search/keyword?api_key={self.apikey}&query={kelime}&page=1")
        
        return cevap.json()
    
    def encokoy(self):
       cevap = requests.get("https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1&region=e35e8781f0006a53ec2bf0ee54b7d04e")
       
       return cevap.json()


filmapi = MoiveDb()

while True:
    secim = input("\n1-popüler filmler\n2-film ara\n3-cikis\nseciminiz: ")

    if(secim=="1"):
        
        filmler = filmapi.popüler()
        
        for film in filmler["results"]:

            print(film["title"])

    elif(secim=="2"):
        kelime = input("aramak istediginiz kelime: ")

        filmler = filmapi.ara(kelime)

        for film in filmler["results"]:

            print(film["name"])

    elif(secim=="3"):
        filmler = filmapi.encokoy()

        print(filmler)

        # for film in filmler:

        #     print(film.text)
    else:
        print("hatali secim yaptiniz")
        break

        # sonda web scraping i anlatıyor