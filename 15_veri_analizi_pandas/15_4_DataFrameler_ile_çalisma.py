import pandas as pd
from numpy.random import randn

df = pd.DataFrame( randn(3,3), index=["A","B","C"], columns=["sütun1","sütun2","sütun3"] ) # 3 e 3 lük satırları sütunları verdik

sonuc = df
sonuc = df["sütun1"]              # sadece sütun1 gelir
sonuc = type(df["sütun1"])        # <class 'pandas.core.series.Series'> tipindedir yani aslında bir pandas serisidir 
sonuc = df[ ["sütun1","sütun2"] ] # sütun1 ve sütun2 gelir

# loc["satır","sütun"] normalde,  loc["satır"] sadece satır    loc[:, "sütun1"] sadece sütun1

sonuc = df.loc["A"]                    # sadece A satırını getiri sütun1 sütun2 ve sütun3 değerini
sonuc = type(df.loc["A"])              # <class 'pandas.core.series.Series'> tipindedir yani pandas serisidir
sonuc = df.loc[:,"sütun1"]             # A 0.690563\n B 0.330798\n C 0.990233 Name: sütun1, dtype float64 bu şekilde yazar
sonuc = df.loc[:,["sütun1","sütun2"] ] # A B C değerleri sütun1 ve sütun 2 için gelir sonuc= df[["sütun1","sütun2"]] bunla aynı çıktı
sonuc = df.loc[:, "sütun1":"sütun3"]   # sütun 1 den sütun 3 e kadar getirir normal df i görürüz yani
sonuc = df.loc[:, :"sütun2"]           # baştan başlar sütun2 ye kadar alır yani sütun1 ve sütun2 yi 0 desen de olur demesen de
sonuc = df.loc["A":"C", :"sütun2"]     # A dan C ye kadar al ve baştan sütun2 ye kadar getir
sonuc = df.loc[:"C", :"sütun2"]        # baştan C ye kadar al ve baştan sütun2 ye kadar getir üsttekinin aynısı

#sonuc = df.loc[2] # hata verir çünkü 2 diye bir index yok biz değiştirdik
sonuc = df.iloc[2] # illa sayıyla çalışmak istersek bu şekilde yapabiliriz 2.indeks yani C yi bize sütun1 2 3 için getirir

sonuc = df.loc["A","sütun2"]   # A.satırının sütun2 ye denk gelen değerini alır matris gibi düşün yani 0.satır 1.sütun
sonuc = df.loc["C","sütun3"]   # C.satırının  2.satırın 2.sütununu aldık o mantıkla düşünürsen
sonuc = df.loc[["A","B"], ["sütun1","sütun2"] ] # A B satırları için sütun1 ve 2 değerlerini getirir 2 ye 2 lik olur yani


df["sütun4"] = pd.Series(randn(3), ["A","B","C"]) # sütun 4 ü ekledik rastgele 3 değer A B ve C satırları için

df["sütun5"] = df["sütun1"] + df["sütun3"]        # sütun 5 i ekledik sütun1 ve sütun3 teki değerlerin toplamı olacak

#df.drop("sütun5")    # hata verir çünkü axis değerini belirtmeliyiz sütun old. söylicez yani

print(df.drop("sütun5",axis=1)) # sütun5 sildik ama ana dataframe objesi değişmedi sadece burdakini değiştirdik
print(df.drop("A",axis=0))      # burda da satır sildik ama yine ana nesne değişmedi onun için alttakini yapıcaz
print(df)                       # değiştirmek istiyorsak bir parametre vermemiz gerekiyor

sonuc = df.drop("sütun5",axis=1, inplace = True ) # inplace ile orijinal nesne üzerinde değişiklik yapılır default u False


print(sonuc)