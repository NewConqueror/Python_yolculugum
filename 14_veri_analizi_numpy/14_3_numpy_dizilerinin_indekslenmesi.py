import numpy as np

sayilar = np.array([0,5,10,15,20,25,50,75])

sonuc = sayilar[5]     # 5.indekstekine 25
sonuc = sayilar[-1]    # tersten 1.elemana 75
sonuc = sayilar[0:3]   # 0 dan 3 e kadar 3 dahil değil yani [0 5 10]
sonuc = sayilar[:3]    # yukarıdakinin aynısı default olarak 0 dan başlıyor
sonuc = sayilar[3:]    # 3.indeksten sona kadar [15 20 25 50 75]
sonuc = sayilar[::]    # baştan sona bütün liste [0 5 10 15 20 25 50 75]
sonuc = sayilar[::-1]  # listeyi ters çevirir [75 50 25 20 15 10 5 0]
sonuc = sayilar[::-2]  # listeyi tersen indeks atlayarak alır [75 25 15 5] şeklinde

sayilar2 = np.array([[0,5,10],[15,20,25],[50,75,85]]) # 3 e 3 lük bir matris yapmış olduk
print(sayilar2)
#        0  1  2
#  0  [[ 0  5 10]
#  1   [15 20 25]
#  2   [50 75 85]]

sonuc = sayilar2[0] # komple 0.satır gelir
sonuc = sayilar2[2] # komple 2.satır gelir

sonuc = sayilar2[0,2] # 0.satırın 2.indeksindeki değer bize gelir yani 10
sonuc = sayilar2[2,1] # 2.satırın 1.indeksindeki değer bize gelir yani 75

sonuc = sayilar2[:,2] # bütün satırlar seç ve onların içinden sadece 2.indekstekileri al yani [10 25 85]

sonuc = sayilar2[:,0] # bütün satırlardan 0.indektekileri bana getir yani [0 15 50 ] yeni bir dizi içinde dikkat et

sonuc = sayilar2[:, 0:2] # bütün satırları seç ve 0 ile 2.indeks arasındakileri bana getir yani 
# [[ 0  5] 
#  [15 20]  
#  [50 75]]     # 2 boyutlu bir dizi olduğuna dikkat et

sonuc = sayilar2[-1,:] # tersten ilk satırın bütün sütunlarını al [50 75 85] gelir


sonuc = sayilar2[:3,:3] # 0 1 2. indeksteki satırları al ve onların 0 1 2. elemanlarını bana getir yani
# [[ 0  5 10]
#  [15 20 25]
#  [50 75 85]]

sonuc = sayilar2[:2,:2] # 0 ve 1.indeksteki satırları al ve onların 0 ve 1. elemanlarını bana getir yani
# [[ 0  5]
#  [15 20]]

print(sonuc)


# dizi1 = np.arange(0,10)  # diziler bir pointer olduğu için adresleri eşitlemiş olduk aslında referans
# dizi2 = dizi1            

# dizi2[0] = 20
# print(dizi1)
# print(dizi2)  # dizi 2 yaptığımız değişikliğin dizi 1 i de değiştirdiğini görürüz çünkü adresler aynı


dizi1 = np.arange(0,10)
dizi2 = dizi1.copy()   # böyle yaparak değerleri eşitledik değer aynı ancak adresleri farklı

dizi2[0] = 20

print(dizi1)
print(dizi2)    # dizi2 de yaptığımız değişikliğin dizi1 i etkilemediğini görürüz