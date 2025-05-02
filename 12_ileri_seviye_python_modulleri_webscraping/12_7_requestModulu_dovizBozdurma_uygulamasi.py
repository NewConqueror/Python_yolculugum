import requests
import json

sonuc = requests.get("https://dovizkurlari-l6vtviaacq-uc.a.run.app/api/doviz")

print(sonuc)
sonuc = json.loads(sonuc.text)

print(sonuc["USD"]["ForexSelling"]) # doların güncel satış fiyatını çektik key 0 1 değil "USD" kelimesi

print("bozdurabileceğiniz dövizler")
for i in sonuc:
    print(sonuc[i]["isim"],"=",sonuc[i]["Kod"])

while True:

    boz = input("bozulan döviz türü: ") # GBP
    varmi = False

    for i in sonuc:
        if(sonuc[i]["Kod"]==boz): # İ = GBP
            
            varmi=True

    kursat = float(sonuc[boz]["ForexSelling"])   # GBP nin forexselling yani 33
            

    if(varmi==False):
        print("hatali döviz türü")
        break

    varmi = False

    al = input("alinan döviz türü: ")  # USD 

    for i in sonuc:
        if(sonuc[i]["Kod"]==al):
            varmi=True

    kural = float(sonuc[al]["ForexBuying"])  # 26.074

    if(varmi==False):
        print("hatali döviz türü")
        break

    nekadar = float(input(f"ne kadar {boz} bozdurmak istiyorsunuz: "))


    print(f"1 {boz} = {kursat/kural} {al}")

    hesap = kursat/kural
    fiyat = nekadar*hesap
    
    print(f"toplam: {fiyat} = {al}")
        






