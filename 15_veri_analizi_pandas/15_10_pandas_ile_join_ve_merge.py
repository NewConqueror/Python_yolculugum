import pandas as pd

müsteri = {
    "musteriId":    [1,2,3,4],
    "ad":    ["ahmet","ali","hasan","canan"],
    "soyad": ["yılmaz","korkmaz","çelik","toprak"]
}

siparis = {
    "siparisId": [10,11,12,13],
    "musteriId":    [1,2,5,7],
    "siparisTarihi": ["2010-02-07","1996-06-27","2004-07-28","1453-06-29"]
}

df_musteri = pd.DataFrame(müsteri, columns=["musteriId","ad","soyad"])
df_siparis = pd.DataFrame(siparis, columns=["siparisId","musteriId","siparisTarihi"])

print(df_musteri)
print(df_siparis)


sonuc = pd.merge(df_musteri, df_siparis, how="inner")  # ortak kayıtları getirir yani musteriId 1 ve 2 olanı

sonuc = pd.merge(df_musteri, df_siparis, how="left")   # sol tarafı yani df_musteri nin hepsini getirir
# karşılığı olmayan siparisId ve siparis tarihi için NaN yazar

sonuc = pd.merge(df_musteri, df_siparis, how="right") # sağ tarafı yani df_siparis in hepsini getirir
# karşılığı olmayan ad ve soyad kısımları için NaN yazar

sonuc = pd.merge(df_musteri, df_siparis, how="outer") # bütün kayıtları getirir
# yukarıdaki left ve right ın birleştirilmiş hali gibi düşün ortaklar 1 kere yazılıyor

sonuc = pd.merge(df_musteri, df_siparis, how="cross") # bir kayıt için diğer bütün kayıtları çaprazlar
# bir adamın 4 kayıtı olur yani



müsteriA = {
    "musteriId":    [1,2,3,4],
    "ad":    ["ahmet","ali","hasan","canan"],
    "soyad": ["yılmaz","korkmaz","çelik","toprak"]
}


müsteriB = {
    "musteriId":    [4,5,6,7],
    "ad":    ["yağmur","çınar","cengiz","can"],
    "soyad": ["bilge","turan","yılmaz","bektaş"]
}

df_musteriA = pd.DataFrame(müsteriA, columns=["musteriId","ad","soyad"])
df_musteriB = pd.DataFrame(müsteriB, columns=["musteriId","ad","soyad"])


sonuc = pd.concat([df_musteriA, df_musteriB]) # axis = 0 satırları alt alta yazar iki kayıt alt alta olur
sonuc = pd.concat([df_musteriA, df_musteriB], axis=1) # sütunları yan yana yazar iki kayıt yan yana olur
print(sonuc)