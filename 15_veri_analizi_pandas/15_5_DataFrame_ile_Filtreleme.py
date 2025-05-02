import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data, columns=["sütun1","sütun2","sütun3","sütun4","sütun5"])

sonuc = df
sonuc = df.columns  # dataframe içerisindeki sütun adlarını bize getirir 
sonuc = df.head()   # default olarak ilk 5 kaydı getirir 0 1 2 3 4 yani
sonuc = df.head(10) # parametre vererek değiştirdik ilk 10 kaydı getirir 0..9
sonuc = df.tail()   # sondan 5 kaydı getirir 14 13 12 11 10
sonuc = df.tail(10) # sondan 10 kaydı getirir 14..5

# aga 5 tane değil 100 tane sütun olabilir ben hepsini görmek istemiyorum napıcam 

sonuc = df["sütun1"]            # sadece sütun 1 i getirir ama baştan sona kadar ya 1000 tane satır olsa
sonuc = df["sütun1"].head()     # sütun 1 den sadece ilk 5 kaydı getirir
sonuc = df.sütun1.head()        # böyle de yapabilirsin ama kafa karıştırıcı olabilir o yüzden üstteki daha iyi
sonuc = df[["sütun1","sütun2"]] # birden fazla sütun görmek istersek liste tipinde göndermek lazım sütun1 sütun2 gelir
sonuc = df[["sütun1","sütun2"]].head() # sütun1 sütun2 için ilk 5 kayıt
sonuc = df[["sütun1","sütun2"]].tail() # sütun1 sütun2 için son 5 kayıt

sonuc = df[5:15] [ ["sütun1","sütun2"] ].head() # 5 ile 15 arasındaki sütun1 ve sütun2 kayıtlarını al ilk 5 tanesini göster
#                                                 5 ten itibaren yani  5 6 7 8 9  gelir
sonuc = df[5:15] [ ["sütun1","sütun2"] ].tail() # yukarının aynısı sondan 14 13 12 11 10 gelir


sonuc = df > 50 #bütün kayıtlara bakar 50 den büyük olanlara True olmayanlara False denir kayıt kadarTrue False un olur
sonuc = df[ df > 50]    # şartı sağlayanlar için sayıları gösterir sağlamayanlar içinse NaN yazar
sonuc = df[ df % 2 ==0] # çift olanlar sayı çift olmayanlar NaN

sonuc = df["sütun1"] > 50  # sadece sütun1 için True False şeklinde gelir diğerleri gösterilmez

sonuc = df[ df["sütun1"] > 50 ] # sütun1 deki değerleri 50 den büyük olan bütün satırları getirir
#                                 yani sütun2 3 4 5 te gelir şart aranmadan

sonuc = df[ df["sütun1"] > 50 ][ ["sütun1","sütun2"] ] # sütun 1 deki değerleri 50 den büyük olan satırları getirir
#                                                        ama sadece sütun1 ve sütun2 yi getirir

sonuc = df[ (df["sütun1"] > 50) & ( df["sütun1"] <=70 ) ] # sütun1 deki değerleri 50 den büyük 70 ten küçük olan
#                                                           satırları getirir yine tüm sütunlar için

sonuc = df[ (df["sütun1"] > 50) | ( df["sütun2"] > 50 ) ] # sütun1 50 den büyük veya sütun2 50 den büyükse getirir bütün satırları

sonuc = df[ (df["sütun1"] > 50) | ( df["sütun2"] > 50 ) ][ ["sütun1","sütun2"] ] # üsttekinden farklı olarak sadece
#                                                                                  sütun1 ve sütun2 yi getirir

sonuc = df.query("sütun1 >=50 & sütun1 % 2 == 0") # bu yöntemle de yapabilirsin sütun1 50 den büyük ve çiftse
#                                                   o satırları getir tüm sütunlar için 


sonuc = df.query("sütun1 >=50 & sütun1 % 2 == 0")[ ["sütun1","sütun2"] ] # aynısı sadece sütun1 ve sütun2 gelir

print(sonuc)
