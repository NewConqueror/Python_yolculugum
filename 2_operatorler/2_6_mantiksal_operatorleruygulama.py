#1 sayi 0 ve 100 arasinda mi
sayi = int(input("sayi: "))
sonuc = 0< sayi <100
print(f"sayi 0 ve 100 arasinda mi {sonuc}")

#2 pozitif ve 2 ye bölünebiliyor mu
sayi = int(input("sayi: "))
sonuc = (sayi>0) and (sayi % 2 ==0)
print(f"sayi pozitif ve çift mi {sonuc}")

#3 email ve parola ile giriş kontrolü yap
email = input("email: ")
parola =input("parola: ")

sonuc = (email=="abcd") and (parola=="1234")
print(f"giris basarili mi {sonuc}")

#4 girilen 3 sayıyı büyüklük olarak karşılaştır
sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))
sayi3 = int(input("sayi3: "))

büyük1 = (sayi1>sayi2) and (sayi1>sayi3) 
büyük2 = (sayi2>sayi1) and (sayi2>sayi3) 
büyük3 = (sayi3>sayi1) and (sayi3>sayi2) 



# 5 2 vize 60 final 40 ortalama hesapla 50 üstü geçer altı kalır
# a) ort 50 olsa bile final en az 50 olmalı 
# b) finalden 70 alırsa direkt geçer
vize1 = int(input("vize1: "))
vize2 = int(input("vize2: "))
final = int(input("final: "))

ort = ( (vize1+vize2) /2 )*0.6 + final*0.4

gectimi = ( (ort>=50) and (final>=50) ) or final>70




# 6 kişinin boy kilo al kilo endeksi hesapla kilo / boy^2

boy = int(input("boy: "))
kilo = int(input("kilo: "))

vke = kilo*(boy**2)

zayif = 0 > vke <= 18.4
normal = 18.5 > vke <=24.9
fazlakilo = 25.0 > vke <= 29.9
obez = 30.0 > vke <= 34.9

