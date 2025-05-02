x = input("1. sayı: ") # kullanıcıdan böyle sayı isteniyormuş
y = input("2. sayı: ") # sayıyı alıcaz direkt x ve y ye aticaz


toplam =x + y #sonuç 1020 çıktı niye çünkü direkt string tipinde aldı string tipinde yazdık çünkü bunu değiştirmek için tip dönüşümü yapmalıyız

print(type(x))
print(type(y)) # burada hangi tipte olduklarını öğreniyoruz string tabii ki

toplam = int(x) + int(y) # burda da tipi ne olursa olsun int a çeviriyoruz

print(toplam) 
# 2. denemede 30 çıkacak çünkü string tipinden int tipine çevirdik

x=5
y=2.5
ad="fatih"
onlinemi=False 

print(type(x))
print(type(y))
print(type(ad))
print(type(onlinemi))
#tiplerini öğrenme


x = float(x) # int x i floata çevirdik
print(x)
print(type(x))

y = int(y) # int x i floata çevirdik
print(y)
print(type(y))

sonuc = str(x) + str(y)
print(sonuc)
print(type(sonuc))

onlinemi = str(onlinemi) # yazı olarak False döndürür
print(onlinemi)
print(type(onlinemi))


onlinemi = int(onlinemi) # 0 döndürür
print(onlinemi)
print(type(onlinemi))