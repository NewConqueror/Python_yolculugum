import pandas as pd
import numpy as np

data = {
    "sütun1": [1,2,3,4,5],
    "sütun2": [10,20,13,20,25],
    "sütun3": ["abc","bcaa","ade","cb","dea"]
}

def kareal(x):
    return x * x

kareal2 = lambda x:  x * x

df = pd.DataFrame(data)

sonuc = df

sonuc = df["sütun2"].unique() # tekrarlayan değerleri getirmez sadece 1 tane getirir 10 20 13 25 yazar 2. 20 yazılmaz
sonuc = df["sütun2"].nunique() # unique yani tekrar etmeyen kaç sayı var onu söyler 4 2. 20 yi saymaz ilkini sayar

sonuc = df["sütun2"].value_counts()         # hangi değerden kaç tane old. söyler 20 2  10 1  13 1  25  1 yazar

sonuc = df["sütun1"] * 2                    # sütun1 deki elemanların karesini alır 1 4 9 16 25
sonuc = df["sütun1"].apply(kareal)          # nesne verir gibi veriyoruz dikkat et fonksiyon verir gibi değil
sonuc = df["sütun1"].apply(kareal2)         # illa fonk a gerek yok lambda ile de yapabilirsin
sonuc = df["sütun1"].apply(lambda x: x * x) # başka yerde kullanmicaksan tek seferlikse böyle de yapabilirsin

sonuc = df["sütun3"].apply(len)             # sütun 3 teki stringlerin kaç elemanlı old. söyler
df["sütun4"] = df["sütun3"].apply(len)      # sütun 3 tekilerin kaç elemanlı old. sütun4 e yazar
# print(df)

sonuc = df.columns                          # sütun bilgilerini bize getirir
sonuc = len(df.columns)                     # kaç tane sütun olduğunu bize söyler  4

sonuc = df.index                            # index hakkında bilgi verir RangeIndex(start=0, stop=5, step=1)
sonuc = len(df.index)                       # kaç tane index yani satır old. bize söyler  5
sonuc = df.info                             # bize dataframe hakkında detaylı bilgi verir

sonuc = df.sort_values("sütun2")                    # değerleri sıralama yapar  default küçükten büyüğe doğru
sonuc = df.sort_values("sütun3")                    # a dan z ye doğru sıralama yapar büyükten küçüğe istersen
sonuc = df.sort_values("sütun3", ascending = False) # normalde True False yapınca büyükten küçüğe sıralicak



data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

df = df.pivot_table(index="Ay", columns="Kategori", values="Gelir")

print(df)
# satırlar  Ay tipinde   sütunlar Kategori tipinde  değerler ise Gelir tipinde olsun dedik
# Kategori  Elektronik  Giyim  Kitap       # çıktısı böyle olur
# Ay
# Haziran           30     36     32
# Mayıs             20     12     14
# Nisan             15     52     42



print(sonuc)