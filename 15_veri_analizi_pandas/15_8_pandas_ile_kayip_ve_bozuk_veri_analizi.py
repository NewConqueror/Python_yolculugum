import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df = pd.DataFrame(data,index=["a","c","e","f","h"], columns=["sütun1","sütun2","sütun3"] )

df = df.reindex( ["a","b","c","d","e","f","g","h"] )  # yeni satırlar ekledik b d g sütunlarında NaN yazıyor

yenisütun = [np.nan,30,np.nan,51,np.nan,20,np.nan,10]

df["sütun4"] = yenisütun

sonuc = df

sonuc = df.drop("sütun1",axis=1)                # sütun1 i sildik
sonuc = df.drop(["sütun1","sütun2"], axis=1)    # sütün1 ve sütun2 yi sildik

sonuc = df.drop("a",axis=0)                     # a satırını sildik
sonuc = df.drop( ["a","b","h"] )        # a b h satırlarını sildik axis default olarak 0 yazmasanda olur ama sen yaz

sonuc = df.isnull()                           # NaN değerleri için True normal değerler için False döndürür
sonuc = df.notnull()                          # Nan değerleri için False normal değerler için True döndürür 

sonuc = df.isnull().sum()                     # sütun1 sütun2 ve sütun3 sütun4 için kaç NaN değer olduğunu söyler
sonuc = df.isnull()["sütun1"].sum()           # sadece sütun 1 için kaç NaN değer olduğunu söyler

sonuc = df[ df["sütun4"].isnull() ]           # sadece sütun 4 için NaN olan satırları getirir diğer sütunlar da gelir
sonuc = df[ df["sütun4"].isnull() ]["sütun4"] # sadece sütun 4 için NaN olan satırları getirir Sadece sütun4
sonuc = df[ df["sütun1"].notnull() ]["sütun1"]# sadece sütun1 için normal  satırları getirir sadece sütun1
sonuc = df[ df["sütun1"].notnull() ]          # sadece sütun1 için normal  satırları getirir diğer sütunlar da gelir


sonuc = df.dropna() # axis = 0 satıra göre eğer satırda bir NaN değer varsa bile o satırı bize getirmez
sonuc = df.dropna(axis=1)    # eğer sütunda bir NaN değer varsa bile o satırı bize getirmez boş döner şuan

sonuc = df.dropna(how="any") # default axis = 0 herhangi bir NaN değer varsa o satırı bize getirmez dropna() ile aynı
sonuc = df.dropna(how="any",axis=1) # herhangi bir NaN değer varsa o sütunu bize getirmez df.dropna(axis=1) ile aynı

sonuc = df.dropna(how="all") # bütun elemanları NaN olan satır varsa o satırı bize getirmez   g yi getirmedi mesela
sonuc = df.dropna(how="all",axis=1) # bütun elemanları NaN olan sütun varsa onu bize getirmez bizde şuan yok

sonuc = df.dropna(subset= ["sütun1","sütun2"], how="all") # sütun1 ve sütun2 de NaN varsa o satır getirilmez ikisi de önemli
sonuc = df.dropna(subset= ["sütun1","sütun2"], how="any") # herhangi birinde NaN varsa o satır getirilmez

sonuc = df.dropna( thresh=2 ) # en az 2 tane normal değer olmalı yoksa o satırı getirme en az sayıda normal veri
sonuc = df.dropna( thresh=4 ) # en az 4 tane normal değer olmalı yoksa o satırı getirme

sonuc = df.fillna(value= "bos") # NaN değerler yerine bos yazar 
sonuc = df.fillna(value= -1)    # NaN değerler yerine -1 yazar

sonuc = df.sum()       # her bir sütunun toplamını verir sütun1 2 3 4 vs
sonuc = df.sum().sum() # direkt bütun sayıların toplamını verir aslında sütun toplamlarını toplar

sonuc = df.size      # toplam eleman sayısını verir ama buna NaN değerler de dahil  32 = 8 e 4 lük
sonuc = df.isnull().sum() # her bir sütunda toplam NaN değerini verir sütun1 3 sütun2 3 vs vs
sonuc = df.isnull().sum().sum() # toplam NaN değerini verir aslında her bir sütundaki NaN toplamını toplar


def ortalama(df):

    toplam = df.sum().sum()
    
    adet = df.size - df.isnull().sum().sum() # toplam sayıdan NaN olanları çıkardık 

    return toplam / adet

sonuc = df.fillna( value= ortalama(df) ) # NaN değerlerini hesapladığımız ortalama ile doldurur


print(sonuc)
