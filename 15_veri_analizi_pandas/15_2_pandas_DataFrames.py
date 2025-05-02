# serilerin devamı gibi 2 seri toplamı bir dataframe excel tablosuna benziyor sql gibi sorgulama yapabiliyon veri analizi aga
# farkı serilerde sütun başlığı yoktu bunda var index her ikisi için de aynı

import pandas as pd

# df = pd.DataFrame()  # Empty DataFrame Columns: [] Index: [] boş old. söyler sütun ve indexler birer liste

# df = pd.DataFrame([1,2,3,4]) # liste verdik sütun ismi vermezsen default olarak sıfır atar index aynı

# df = pd.DataFrame([ ["ahmet",50], ["ali",60], ["yağmur",70] ["çınar",80] ])# her bir eleman bir satırı temsil eder 0 1 atar sütunlara

liste = [ ["ahmet",50], ["ali",60], ["yağmur",70],["cinar",80] ]

df = pd.DataFrame(liste, columns = ["ad","notlar"],index=[111,222,333,444])
df = pd.DataFrame(liste, [111,222,333,444],["ad","notlar"]) # tanımlamazsan colum index vs diye default şekli böyle
df = pd.DataFrame(liste, index=[111,222,333,444],columns=["ad","notlar"],dtype=float) 
# index şu column şu dersen önemi kalmıyor sıranın her türlü çalışıyor float tipinde olsun da dedik


# dict yapısı oluşturursam işler çok daha basit olur

dict = {"ad": ["ahmet","ali","yağmur","cinar"], "notlar": [50,60,70,80] } # ad sütun notlar sütun elemanları da liste içindekiler

df = pd.DataFrame(dict)
df = pd.DataFrame(dict, index=[111,222,333,444])

dict_list = [
                {"ad":"ahmet" ,"notlar":50},     # her bir eleman bir satıra karşılık gelir
                {"ad":"ali"   ,"notlar":60},
                {"ad":"yağmur","notlar":70},
                {"ad":"cinar" ,"notlar":80},

            ]

df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index=[111,222,333,444])

print(df)

# s1 = pd.Series([1,2,3,4,5])
# s2 = pd.Series([6,7,8,9,0])

# data = dict(apples = s1, oranges = s2)    apples sütununda s1   oranges sütununda s2 elemanları olur index aynı
  
# df = pd.DataFrame(data)

# print(df)




