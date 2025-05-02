names = ["ali","yağmur","hakan","deniz"]
years = [1998,2000,1998,1987]

# 1 - cenk ismini listenin sonuna ekleyiniz
sonuc = names.append("cenk")

# 2 - sena değerini listenin başına ekleyiniz
sonuc = names.insert(0,"sena") # names.insert(-1,"fatih") sondan bir öncekine names.insert(len(names),"mehmet") bu harbi sona ekler

# 3 - deniz ismini listeden siliniz
# sonuc = names.remove("deniz") # sonuc = names.pop() # en sonda olduğu için bu da işe yarar
# sonuc = names.pop(3) 3.indisteki elemanı döndürür ve siler o da deniz 


# 4 - deniz isminin indeksi nedir
sonuc = names.index("deniz") 

# 5 - ali listenin bir elemanı mıdır
sonuc = "ali" in names # sonuc = names.index("ali") ali varsa index döndürür yoksa -1 döndürür

# 6 - liste elemanlarını ters çevirin
sonuc = names.reverse()

# 7 - liste elemanlarını alfabetik olarak sıralayın
sonuc = names.sort()

# 8 - years listesini rakamsal büyüklüğe göre sıralayın
sonuc = years.sort()
sonuc = years.reverse()

# 9 - str = "chevrolet,dacia" karakter dizisini listeye çeviriniz split kullan
str = "chevrolet,dacia"
dizi = str.split(",")

print(dizi)

# 10 - years dizisinin en büyük ve en küçük elamanı nedir
buyuk = max(years)
kucuk = min(years)

# 11 - years dizisinde kaç tane 1998 değeri vardır
sonuc = years.count(1998)

# 12 - years dizisinin tüm elamanlarını siliniz
sonuc = years.clear()

# 13 - kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız
markalar = [] # markalar diye bir dizi oluşturduk bu kullanımı bil

birinci = input("bir marka giriniz: ")
ikinci = input("bir marka giriniz: ")
ucuncu = input("bir marka giriniz: ")

markalar.append(birinci)
markalar.append(ikinci)
markalar.append(ucuncu)

print(markalar)