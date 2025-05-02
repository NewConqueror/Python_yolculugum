import numpy as np

sayilar1 = np.random.randint(10,100,6)
sayilar2 = np.random.randint(10,100,6)

print(sayilar1)
print(sayilar2)

sonuc = sayilar1 + sayilar2  # aynı indekstekileri toplar ör s1 0. 10 s2 0. 20 yeni dizi de 0. 30 olur
sonuc = sayilar1 + 10        # sayilar1 dizisindeki sayilara 10 ekler
sonuc = sayilar1 - sayilar2  # aynı indekstekileri çıkarır ör s1 0. 10 s2 0. 20 yeni dizi de 0. -10 olur
sonuc = sayilar1 - 10        # sayilar1 dizisindeki indekslerden 10 çıkarır
sonuc = sayilar1 * sayilar2  # aynı indekstekileri çarpar
sonuc = sayilar1 * 10        # sayıları 10 ile çarpar
sonuc = sayilar1 / sayilar2  # aynı indekstekileri böler
sonuc = sayilar1 / 10        # sayıları 10 a böler

sonuc = np.sin(sayilar1)     # sayilarin sinüsünü      alır
sonuc = np.cos(sayilar1)     # sayilarin cosinüsü      alır
sonuc = np.sqrt(sayilar1)    # sayilarin karekökünü    alır
sonuc = np.log(sayilar1)     # sayilarin logaritmasını alır



multi_sayilar1 = sayilar1.reshape(2,3)   # 2 ye 3 lük olarak tekrar şekil verdik yani 2 satır 3 sütun
multi_sayilar2 = sayilar2.reshape(2,3)   # 2 ye 3 lük olarak tekrar şekil verdik yani 2 satır 3 sütun

# print(multi_sayilar1)
# print(multi_sayilar2)

sonuc = np.vstack((multi_sayilar1,multi_sayilar2))
# 1.matris [52 81 75 64 46 35]
# 2.matris [45 16 92 42 41 26]

# multi 1.matris [[52 81 75]
#                 [64 46 35]]
# multi 2.matris [[45 16 92]
#                 [42 41 26]]

# [[52 81 75]  vstack ile yaparsak direkt 1.matrisin altına 2.matrisi ekler
#  [64 46 35]
#  [45 16 92]
#  [42 41 26]]

sonuc = np.hstack((multi_sayilar1,multi_sayilar2))
# 1.matris [73 31 95 44 54 56]
# 2.matris [45 90 64 79 94 92]

# multi 1.matris [[73 31 95]
#                 [44 54 56]]
# multi 2.matris[[45 90 64]
#                [79 94 92]]

#  [[73 31 95 45 90 64]   hstack ile yaparsak 2.matrisi 1.matrisin yanına ekler
#  [44 54 56 79 94 92]]   


sonuc =  sayilar1 >=50 # sayilar1 in büün elemanlarına bakar ve 50 den büyük olanlar için True az olanlar için False döndürür
#                       [49 89 44 20 73 17] [False  True False False  True False] dikkat et liste şeklinde True False 

sonuc = sayilar1 % 2 ==0 # çift olanlar için True tek olanlar için False değerini döndürür
#                        # hangi indekstekiler True aga hangi sayılarla onları da görmek istersem

print(sayilar1[sonuc]) #      [37 70 58 25 20 20]             
print(sonuc) #           [False  True  True False  True  True]  [70 58 20 20] True olanlar