# paket pythonda yok kendimiz indiricez pip install request yazarak

import requests # ne işe yaricak bir http requesti yapabiliyorsun bir int sitesinin adresini yazdığında bu int sitesinin
# html kodlarına bu request paketi ile ulaşabilirsin bir websitesine python ile talep yapabiliyorsun olay bu

sonuc = requests.get("https://jsonplaceholder.typicode.com/todos")
print(sonuc) # bize Response [200] döndürücek bu bize başarılı olduğumuzu söyler her şey yolunda
# benim amacım ordaki json bilgileri alabilmek

sonuc = sonuc.text

print(sonuc) # bize bütün dokümanı gösterri

print(type(sonuc)) # bize str yani string bir bilgi olduğunu söyler

print(sonuc[0]["title"]) # bunu yapamayız json string tipinde ama sen dict gibi davranıyon olmaz

import json

# bize json string tipinde gelen bir veriyi python un anlayacağı bir dict yapısına çevirelim

sonuc = requests.get("https://jsonplaceholder.typicode.com/todos")

sonuc = json.loads(sonuc.text)

print(sonuc[0]["title"]) # artık yapabilirsin dict e çevirdik
print(sonuc[0])

print(sonuc) # her kaydı gösterir karmakarışık filtreleme yapabiliriz

for i in sonuc:
    if(i["userId"] == 1):
        print(i) # bütün bilgiler satır satır karşımıza gelir
        print(i["title"])

# bir web sayfasına request te talepte bulunduk bize bir json bilgisi gönderdi listeye çevirdik
#hmtl kaynağı içindeki bütün bilgileri anlıp onlarla işlem yapabilirz web sitesi yapabiliriz mobil masaüstü
# uygulamada gösterebiliriz