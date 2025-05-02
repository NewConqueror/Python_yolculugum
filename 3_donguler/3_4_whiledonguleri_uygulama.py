sayilar = [1,3,5,7,9,12,19,21]

# while ile yazdir

uzunluk = len(sayilar)
x = 0

while x <uzunluk:
    print(sayilar[x])
    x+=1


# başlangıç bitiş al aradaki tüm tek sayıları yazdır

baslangic = int(input("baslangic: "))
bitis = int(input("bitis: "))

while baslangic <=bitis:
    if(baslangic % 2 !=0):
        print(baslangic)
    baslangic+=1



# 1 100 arasında azalan yazdır
a=100
while a > 0:
    print(a)
    a-=1 

# aldığın 5 sayıyı ekranda sıralı yazdır

numbers = []
i=0

while i < 5 :
    num = int(input(f"{i+1}. sayiyi giriniz: "))
    i+=1
    numbers.append(num)
numbers.sort()
print(numbers)


# sayiyi kullanıcıya sor 
# dictionary kullan (urun, fiyat)
# ekleme bittiğinde while ile listele
# alacağın sınırsız ürün bilgisi urunler listesi içinde sakla

adet = int(input("kac adet urun gireceksiniz: ") )
sayac=0

urunler = []

while sayac <=adet :
    ad = input("urun adi: ")
    fiyat = int(input("urun fiyati: "))

    urunler.append({
        "adi: ": ad,
        "fiyati: ": fiyat
    })

    sayac+=1

# for ile bu şekilde hoca böyle yaptı

for urun in urunler:
    print(f"urun adi: {urun['adi: ']} urunun fiyati: {urun['fiyati: ']}")
    # dışta "" tırnak kullandık içte de "" kullanırsak hata verir o yüzden içte '' kullandık
    print(f'urun adi: {urun["adi: "]} urunun fiyati: {urun["fiyati: "]}')
    # bu da yine aynı işi yapar dışta '' içte "" kullandık sadece tek türde kullanırsak hata alırdık

#print(f"urun adi: {urun["adi: "]} urunun fiyati: {urun["fiyati: "]}")  ikisi de hatalı kullanımdır
#print(f'urun adi: {urun['adi: ']} urunun fiyati: {urun['fiyati: ']}')  tek tip olmaz içte farklı dışta farklı olmalı

# while ile bu şekilde bunu ben yaptım hehe
i=0

while i < adet:

    print(f"urun adi: {urunler[i]} urunun fiyati: {urunler[i+1]}")
    i+=1




