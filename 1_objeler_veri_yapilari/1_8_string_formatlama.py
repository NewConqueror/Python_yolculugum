ad = "fatih"
soyad ="yeni"

print("benim adim {} {}".format(ad,soyad))
print("benim adim {1} {0}".format(ad,soyad))
print("benim adim {s} {a}".format(a=ad,s=soyad))
print("benim adim {} {} ve ben {} yasindayim".format(ad,soyad,"18"))
age=18
print("benim adim {} {} ve ben {} yasindayim".format(ad,soyad,age))

sonuc = 200/700
print("sonuc: {s}".format(s=sonuc))
print("sonuc: {s:1.3}".format(s=sonuc))  # burda toplam değil virgülden önceki ne kadar olsun onu seçtik
print("sonuc: {s:10.5}".format(s=sonuc))  # toplam 10 virgülden sonra 5 basamak

print(f"benim adim {ad} {soyad} ve ben {age} yasindayim".format(ad,soyad,age))