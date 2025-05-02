import numpy as np

sonuc = np.array([1,3,5,7,9]) # biz veririz listeyi diziye çevirir direkt [1 3 5 7 9]

sonuc = np.arange(1,10)  # 1 den 10 a kadar bir dizi oluşturur yani [1 2 3 4 5 6 7 8 9 ] şeklinde

sonuc = np.arange(10,100,5) # 10 dan 100 e kadar 5 er artarak diziyi oluşturur [10 15 20 ... 95]

sonuc = np.zeros(10)  # sadece 0 lardan oluşan 10 elemanlı bir dizi oluşturur ama float değerler olur 0.

sonuc = np.ones(10) # aynı şekilde sadece 1 lerden oluşan 10 elemanlı bir dizi float değerler 1. şeklinde

sonuc = np.linspace(0,100,5) # 0 dan 100 e git ama 5 eş parçaya böl çıktısı -> [0. 25. 50. 75. 100.] float yine

sonuc = np.linspace(0,5,5)  # 0 dan 5 e 5 eş parçaya böl  çıktısı  [0. 1.25 2.5 3.75 5.] şeklinde olur

sonuc = np.random.randint(0,10) # 0 ile 9 arasında rastgele int sayı döndürür

sonuc = np.random.randint(20)   # 0 ile 19 arasında sayılar verir  alt sınır default olarak 0 dan başlar

sonuc = np.random.randint(1,10,3) # 1 il 9 arasında rastgele 3 elemanlı bir DİZİ oluşturur [ 6 9 1 ] vs vs 

sonuc = np.random.rand(5) # 0 ile 1 arasında 5 tane rastgele sayı üret [0.982 0.712 0.220507 0.86277911 0.05904654] vs

sonuc = np.random.randn(5) # bu sefer - sayılar da yazılır [ 0.51315182  0.3 -0.09461052 -0.18982556  0.60036154] vs vs

np_multi = np.arange(50) # 0 dan 49 a kadar olan bir dizi döndürür

sonuc = np_multi.reshape(5,10) # 5 e 10 luk yani 5 satır 10 sütundan olan bir matrise çevirdik yeniden şekil verdik
# [[ 0  1  2  3  4  5  6  7  8  9]
#  [10 11 12 13 14 15 16 17 18 19]
#  [20 21 22 23 24 25 26 27 28 29]
#  [30 31 32 33 34 35 36 37 38 39]
#  [40 41 42 43 44 45 46 47 48 49]]


# print(np_multi.sum(axis=1)) # satırların toplamını getirir [ 45 145 245 345 445] şeklinde ama şuan hatalı çalışma şeklini bulman gerekiyor

#print(np_multi.sum(axis=0)) # sütunların toplamını getirir [ 100 105 110 115 120 125 130 135 140 145 ] şeklinde


rnd_number = np.random.randint(1,100,10) # 1 den 100 e kadar rastgele 10 sayı üret bir dizi oluşturur
print(rnd_number)

sonuc = rnd_number.max()  # dizi içinden en büyük elemanı getirir

sonuc = rnd_number.min()  # dizi içinden en küçük elemanı getirir

sonuc = rnd_number.mean() # dizinin ortalamasını getirir

sonuc = rnd_number.argmax() # en büyük elemanın index ini getirir

sonuc = rnd_number.argmin() # en küçük elemanın index ini getirir   
print(sonuc)
