# isim yaş eğitim ehliyet alabiliyor mu 18 lise veya üni

ad = input("ad: ")
yas = int(input("yas: "))
egitim = input("egitim durumu: ")

if ( (yas>18) )and (egitim=="lise" or egitim=="üni"):
    print("ehliyet alabilir")
else:
    print("ehliyet alamaz")
   

if (yas>18):
    if (egitim=="lise" or egitim=="üni"):
        print(f" {ad} ehliyet alabilir")
    else:
        print(f" {ad} ehliyet alamazsiniz egitiminiz yetersiz")
else:
    print(f" {ad} ehliyet alamazsiniz yasiniz tutmuyor")
   

# 2 yazılı 1 sözlü ort sonra 1 2 3 vs
yazili1 = int(input("yazili1: "))
yazili2 = int(input("yazili2: "))
sozlu = int(input("sozlu: "))

ort = (yazili1+yazili2+sozlu)/3

if (0 < ort <= 24):
    print("0")
elif (24<  ort <=44):
    print("1")
elif (44<  ort <=54):
    print("2")
elif (54<  ort <=69):
    print("3")
elif (69<  ort <=84):
    print("4")
elif (84<  ort <=100):
    print("5")
else:
    print("hatali bilgi girdiniz")

# trafiğe çıkış tarihini al  servis zamanınu bul
# 1.bakım 1.yıl
# 2.bakım 2.yıl
# 3.bakım 3.yıl

# süre hesabını alınan gün ay yıl bilgisine göre gün bazlı hesaplayın
# datetime modülünü kullanmak gerekiyor
# (simdi) - (2018/8/1) => gün 


import datetime

tarih = input("araciniz hangi tarihte trafiğe çıktı (2023/6/20): ")

tarih = tarih.split("/") # tarihi yil ay ve gün e göre ayırıp diziye çevirdik [2023,6,20] şeklinde

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2])) # yili ayi ve günü atadik
simdi = datetime.datetime.now() # şimdinin tarihini aldık

fark = simdi - trafigeCikis  # aradaki fark ı bulduk

gun = fark.days  # farkta saniye dakika vs de vardı onları göz ardı edip sadece gün olarak farkı aldık


if gun<=365:
    print("1.servis araligi")
elif gun > 365 and gun < 365*2:
    print("2.servis araligi")
elif gun > 365*2 and gun < 365*3:
    print("3.servis araligi")
else:
    print("hatali süre") #date time olmadan anca böyle


