import pandas as pd
import numpy as np

# kadıköy de yaşayanları, insan kaynaklarında çalışanları vs gruplayabiliriz
personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
# print(df)

sonuc = df
sonuc = df["Maaş"].sum()  # bütün çalışanların toplam maaşını gösterir ben departmana göre bakmak istiyorum

sonuc = df.groupby("Departman") #geriye bir groupby objesi döndürür bu obje üzerinde işlem yapmamız gerekiyor <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000010BE5211290> 

sonuc = df.groupby("Departman").groups # departmana göre grupla dedik {'Bilgi İşlem': [1, 4], vs vs
sonuc = df.groupby( ["Departman","Semt"] ).groups # hem departmana hem semte göre grupla dedik

# semtler = df.groupby("Semt")  # semt e göre grupladık
# print(semtler.groups)         # neyi dolaştığımızı bilek

# for ad,grup in semtler:       # semt e göre grupladığımızı döndük ve yazdırdık
#     print(ad)
#     print(grup)

# for ad,grup in df.groupby("Semt"): # yukarının aynısı extra değişkene gerek kalmıyor
#     print(ad)
#     print(grup)


# for ad,grup in df.groupby("Departman"):
#     print(ad)
#     print(grup)


sonuc = df.groupby("Semt").get_group("Kadıköy")       # sadece semt i kadıköy olanları yazdırdık
sonuc = df.groupby("Departman").get_group("Muhasebe") # sadece departmanı muhasebe olanları yazdırdık

sonuc = df.groupby("Departman").sum()             # It nin ik nın muhasebenin yaş ve maaş toplamını verir
# sonuc = df.groupby("Departman").mean()          # ortalamasını verir ama şuan hatalı çalışıyor
# sonuc = df.groupby("Departman")["Maaş"].mean()  # sadece departmanların maaş ortalaması gelir yaş ort u değil
# sonuc = df.groupby("Departman")["Yaş"].mean()   # sadece yaş ortalaması gelir maaş ort değil

# sonuc = df.groupby("Semt")["Maaş"].mean()       # semte göre maaş ortalaması gelir
# sonuc = df.groupby("Semt")["Yaş"].mean()        # semte göre yaş ortalaması gelir
sonuc = df.groupby("Semt")["Çalışan"].count()     # semte göre çalışan sayısını verir
sonuc = df.groupby("Departman")["Yaş"].max()      # departamana göre max yaşı getirir
sonuc = df.groupby("Departman")["Maaş"].min()     # departamana göre min maaşı getirir
sonuc = df.groupby("Departman")["Maaş"].max()     # departamana göre max maaşı getirir
sonuc = df.groupby("Departman")["Maaş"].max()["Muhasebe"] # sadece muhasebe departmanındaki max maaşı verir
# result = df.groupby("Departman").agg(np.mean)             # bütün departmanlara göre maaş ve yaş ortalaması alır
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]) #bütün departmanların maaş toplamı ort max min görülür
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"] # yukarıdaki ama sadece muhasebe departmanı için

print(sonuc)