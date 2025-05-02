import pandas as pd

pandas_series = pd.Series()
print(pandas_series)       # Series([], dtype: object) boş bir dizi aslında tek boyutlu bir liste tanımlıyoruz

# data 

sayilar = [20,30,40,50]

pandas_series = pd.Series(sayilar)
print(pandas_series)# böyle çıktı verir biz demesek bile kendi 0 1 2 3 diye key değerleri atar
# 0  20  1  30  2  40  3    50 dtype: int64


harfler = ["a","b","c",20] # numpy gibi homojen olmak zorunda değil
pandas_series = pd.Series(harfler)# illa int olması gerekmiyor stringlere de aynı işlemi yapıyor
print(pandas_series)                 # 0 a  1  b  2  c  3  20  dtype: object


skaler = 5
pandas_series = pd.Series(skaler) # direkt 0 5 getirir 1 elemanlı olduğu için
print(pandas_series)


pandas_series = pd.Series(5, [0,1,2]) # 0  5  1  5  2  5  şeklinde çıktı verir
print(pandas_series)


pandas_series = pd.Series(sayilar, ["A","B","C","D"])  
print(pandas_series)  # A 20 B 30 C 40 D 50 şeklinde olur

dictionary = {"a":10,"b":20,"c":30,"d":40}
pandas_series = pd.Series(dictionary)  # zaten dict yapısına çok benzer kolayca oluşturulur 

import numpy as np   # pandasla birlikte kullanılabilir alternatif değil birbirlerine yardımcıdırlar

random_sayilar = np.random.randint(10,100,6)
pandas_series = pd.Series(random_sayilar) # yine aynı 0 1 2 diye oto atar


pandas_series = pd.Series([20,30,40,50], ["a","b","c","d"])

sonuc = pandas_series[0]             # arkada sayı vermiş gibi aynen çalışır 20 gelir
sonuc = pandas_series[-1]            # 50
sonuc = pandas_series[:2]            # a   20    b     30 şeklinde gelir diğerlerinin aksine
sonuc = pandas_series[-2:]           # c   40    d     50 gelir   2 li olunca böyle demek ki
sonuc = pandas_series["a"]           # a ya karşılık gelen 20 değeri gelir
sonuc = pandas_series["d"]           # d ye karşılık gelen 50 değeri gelir
sonuc = pandas_series[["a","c","d"]] # dersek  a   20   c   40 getirir   e için  hata verir
sonuc = pandas_series.ndim           # kaç boyutlu olduğunu bize söyler 1
sonuc = pandas_series.dtype          # dtype bize söyler int64 object vs vs
sonuc = pandas_series.shape          # bize kaça kaç olduğunu söyler (4, )  4 e 1 yani 4 elemanlı 1 boyutlu
sonuc = pandas_series.sum()          # sayıları toplar bize söyler 20 + 30 + 40 + 50 = 140 yani
sonuc = pandas_series.max()          # max değeri bize söyler yani 50
sonuc = pandas_series.min()          # min değeri bize söyler yani 20
sonuc = pandas_series + pandas_series# sayıları toplar a 20 b 30 vs yerin a 40 b 60 c 80 d 100 vs
sonuc = pandas_series + 50           # bütün elemanlara 50 ekler  a 70 b 80 c 90 d 100 vs
sonuc = np.sqrt(pandas_series)       # kareköklerini alır

sonuc = pandas_series >=40
sonuc = pandas_series % 2 == 0

print(pandas_series[pandas_series % 2 ==0]) # yukarı ile aynı şey


opel2018 = pd.Series([10,20,30,40], ["astra","corsa","mokka","insigne"])
opel2019 = pd.Series([40,30,20,10], ["astra","corsa","granland","insigne"])

toplam = opel2018 + opel2019 
print(toplam)          # mokka nın 2. de karşılığı olmadığı için ve granland in 1.de karşılığı olmadığı için Nan yazar
print(toplam["corsa"]) # sadece corsanın bilgisini gösterir
print(toplam["lala"])  # böyle bir şey olmadığı için hata verir